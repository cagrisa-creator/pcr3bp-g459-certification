# R16 quick audit bundle

Run from a clean extraction with Python 3.10+:

```bash
python3 scripts/QUICK_AUDIT.py
```

Expected final line:

`PASS_QUICK_AUDIT_R16`

The script fails closed on a missing package, SHA-256 mismatch, invalid ZIP, exact-parameter mismatch, or any audited theorem-core count/status mismatch. It is a compact integrity/accounting audit; the complete numerical replay is specified separately in `REPRODUCE_R16_WORKING_SPEC_20260926`.
