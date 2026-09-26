#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys, zipfile
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVID = ROOT / 'evidence'
EXPECTED = {
 'R16_FIXED_TRUST_BASE_I2_EVIDENCE_20260926.zip':'c2e1ebb556e991d2d07a1c1e579c61ebe3be8eab143b7cedf9eadd5e814ab76d',
 'R16_D1_I2_GLOBAL_MPFR_REPLAY_20260925.zip':'6f2f8cfbf13817dab25689a4ba8821573ad79f1a53c33454f7e1656119444e77',
 'R16_N0_TWO_COMPONENT_SEMANTICS_AUDIT_20260925.zip':'772f4d994c4a995240ac67892e8d963f3f30703076b238e35bc94d79f8257191',
 'R16_N1_I2_EVIDENCE_PACKAGE_FINAL_20260926.zip':'d7dc02a37bb1480e1b37a123a2c1b035a32ef0d7eebc5af07e43dccc91b611c0',
 'R16_N3_I2_AUTHORITATIVE_EVIDENCE_20260926.zip':'119f4771af2abc22fa582f6cc6df0ad583d22e214526380d1f112edc1ff8330a',
 'R16_N4_I2_AUTHORITATIVE_EVIDENCE_20260926.zip':'fefb2caa2e9371584687616099160f0b0a865eca03661b5878fd7e871f60f5f3',
 'R16_N5_I2_AUTHORITATIVE_EVIDENCE_20260926.zip':'999033ed462bd788b718eff6ce6c5a94117fad49b31e20de4c11fb969f9176ce',
 'R16_FINAL_ENTRY_ASSEMBLY_I2_EVIDENCE_20260926.zip':'3a1ec9850f8127635b9c7a4205ffe9e588515f08b31285ca94862a777286c5d8',
 'R16_COMPLEMENTARY_TRUST_BASE_I2_EVIDENCE_20260926.zip':'53bd25304a10c6d3b932f2a6c8787dd9e91b2f16aee0bc8c7e0e01455bdef5eb',
}

def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def member_json(z: zipfile.ZipFile, suffix: str):
    matches=[n for n in z.namelist() if n.endswith(suffix)]
    assert len(matches)==1, (suffix,matches)
    return json.loads(z.read(matches[0]))

def check_zip(name: str):
    p=EVID/name
    assert p.is_file(), f'missing {p}'
    got=sha256(p)
    assert got==EXPECTED[name], (name,got,EXPECTED[name])
    with zipfile.ZipFile(p) as z:
        bad=z.testzip()
        assert bad is None, (name,bad)
    return p

def exact_parameter_check():
    g=F(459,1000)
    mu_small=g**3*(g**2-3*g+3)/(1-2*g+g**2+2*g**3-g**4)
    mu_article=1-mu_small
    x=mu_article-g
    cL1=x*x/F(2)+(1-mu_small)/(1-g)+mu_small/g
    cstar=cL1+F(1,10000)
    assert mu_article==F(264377992475701,441699674239000)
    assert mu_small==F(177321681763299,441699674239000)
    assert cL1==F(388389323017759836541758,195098602222838720229121)
    assert cstar==F(3884088328779821204137809121,1950986022228387202291210000)
    assert cstar-cL1==F(1,10000) and -cstar < -cL1

def main():
    for n in EXPECTED: check_zip(n)
    exact_parameter_check()

    with zipfile.ZipFile(EVID/'R16_FIXED_TRUST_BASE_I2_EVIDENCE_20260926.zip') as z:
        a=member_json(z,'R16_FIXED_TRUST_BASE_AUDIT_20260926.json')
        assert a['status']=='R16_FIXED_TRUST_BASE_PASS'
        assert a['F0']['status']=='I2_PASS'
        assert a['F1']['status'].startswith('I2_PASS')

    with zipfile.ZipFile(EVID/'R16_D1_I2_GLOBAL_MPFR_REPLAY_20260925.zip') as z:
        a=member_json(z,'R16_D1_GLOBAL_MPFR_REPLAY_AUDIT.json')
        assert a['status'].startswith('PASS_R16_D1_I2')
        assert (a['global_ok'],a['global_fail'],a['global_pass'],a['global_outside'])==(15364,0,13612,1752)
        assert a['r16_expected_pass_verified_ok']==4207 and a['r16_expected_pass_verified_fail']==0
        assert a['global_min_pass_lower_bound']>0

    with zipfile.ZipFile(EVID/'R16_N0_TWO_COMPONENT_SEMANTICS_AUDIT_20260925.zip') as z:
        a=member_json(z,'R16_N0_EXACT_SEMANTICS_AUDIT.json')
        assert a['status']=='PASS' and a['gate_count']==35
        assert all(v['pass'] for v in a['gates'].values())
        assert a['time_factor_A_min']=='541/2000' and a['time_factor_B_min']=='459/2000'

    with zipfile.ZipFile(EVID/'R16_N1_I2_EVIDENCE_PACKAGE_FINAL_20260926.zip') as z:
        a=member_json(z,'R16_N1_I2_FINAL_AUDIT_20260926.json')
        assert a['status']=='PASS_N1_END_TO_END_I2'
        assert a['mathematical_state']['canonical_parent_count']==32661
        assert a['mathematical_state']['pass']==32661 and a['mathematical_state']['pending']==0
        m=a['old_pass_layer_repair']['missing_46_roots']
        assert m['repair_cells']==92 and m['closed_cells']==92 and m['unresolved']==0
        # Recompute the final 92-cell exact dyadic cover directly from the portable final ledger.
        ledger=member_json(z,'R16_MISSING46_REPAIR_FINAL_LEDGER.json')
        assert len(ledger)==1857 and all(r['cert'].get('pass') for r in ledger)
        from collections import defaultdict
        cells=defaultdict(list)
        for r in ledger: cells[int(r['cell'])].append(r)
        assert set(cells)==set(range(92))
        for c,rows in cells.items():
            paths=[r['node']['repair_path'] for r in rows]
            assert len(paths)==len(set(paths))
            sp=sorted(paths)
            assert not any(b.startswith(a) for a,b in zip(sp,sp[1:]))
            weight=sum((F(1,2**int(r['node']['repair_depth'])) for r in rows),F(0))
            assert weight==1,(c,weight)

    with zipfile.ZipFile(EVID/'R16_N3_I2_AUTHORITATIVE_EVIDENCE_20260926.zip') as z:
        raw=z.read([n for n in z.namelist() if n.endswith('AUTHORITATIVE_AUDIT.out')][0])
        a=json.loads(raw)
        assert a['status']=='PASS_N3_I2_AUTHORITATIVE'
        assert a['final_closed_count']==1222 and a['canonical_key_order_match']
        assert a['unweighted_close']==1212 and a['weighted_close']==9 and a['idx582_displacement']['pass']

    with zipfile.ZipFile(EVID/'R16_N4_I2_AUTHORITATIVE_EVIDENCE_20260926.zip') as z:
        a=member_json(z,'n4_independent_graph_audit.json')
        assert a['status']=='PASS_N4_I2_NUMERICAL_AND_GRAPH'
        assert a['half_phase_pass']==30 and a['half_phase_obligations']==30
        assert a['acyclic'] and a['self_edges']==0 and a['theta_monotonic_violations']==0
        assert a['max_longest_hard_edge_path']==5

    with zipfile.ZipFile(EVID/'R16_N5_I2_AUTHORITATIVE_EVIDENCE_20260926.zip') as z:
        a=member_json(z,'R16_N5_I2_AUTHORITATIVE_AUDIT_20260926.json')
        assert a['status']=='R16_N5_I2_PASS'
        assert a['strong_window']['pass']==2392 and a['strong_window']['min_certified_A2']>a['strong_window']['threshold']
        assert a['outer_exact_residual_exclusion']['safe_pass']==2362 and a['outer_exact_residual_exclusion']['hard_sink_pass']==10
        assert a['detachment']['pass']==2372 and a['detachment']['min_theta_dot']>0 and a['detachment']['min_endpoint_margin_rad']>0
        assert a['visit_bridge']['min_visits']==504 and a['visit_bridge']['max_visits_per_cluster']==7 and a['visit_bridge']['min_clusters']==72

    with zipfile.ZipFile(EVID/'R16_FINAL_ENTRY_ASSEMBLY_I2_EVIDENCE_20260926.zip') as z:
        a=member_json(z,'R16_FINAL_ENTRY_ASSEMBLY_AUDIT_20260926.json')
        assert a['status']=='R16_FINAL_ENTRY_ASSEMBLY_PASS'
        assert all(a['checks'].values())
        assert a['proof_nodes']['S2']=='PASS_16_OF_16'
        assert a['exact_arithmetic']['upperA_pair_margin']=='3/20000'
        assert a['exact_arithmetic']['upperTheta_pair_margin_decimal']>0

    with zipfile.ZipFile(EVID/'R16_COMPLEMENTARY_TRUST_BASE_I2_EVIDENCE_20260926.zip') as z:
        a=member_json(z,'R16_COMPLEMENTARY_TRUST_BASE_I2_AUDIT_20260926.json')
        assert a['status']=='R16_COMPLEMENTARY_TRUST_BASE_I2_PASS'
        for k in ['C0','C1','C2','C3','C4']: assert a[k]['status']=='I2_PASS'
        assert a['C0']['exact_cover_cells']==16 and a['C0']['pointwise_beta001_cells']==14
        assert a['C2']['beta_pass_leaves']==1636 and a['C2']['beta_failures']==0
        assert a['C3']['jobs']==50 and a['C3']['pass_leaves']==64300 and a['C3']['failures']==0
        assert a['C4']['beta0_s04_leaves']==8056 and a['C4']['beta0_s06_leaves']==20801
        assert a['C4']['refined_children_pass']=='320/320'
        assert a['terminal_checker']['boxes']==130848 and a['terminal_checker']['fail_chunks']==0

    print('PASS_QUICK_AUDIT_R16')
    print(f'packages={len(EXPECTED)} exact_parameter=PASS theorem_core=PASS')

if __name__=='__main__':
    try: main()
    except Exception as e:
        print('FAIL_QUICK_AUDIT_R16',repr(e),file=sys.stderr)
        raise
