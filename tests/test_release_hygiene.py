from pathlib import Path
def test_no_pycache():
 root=Path(__file__).resolve().parents[1]; assert not any('__pycache__' in p.parts or p.suffix=='.pyc' for p in root.rglob('*'))
