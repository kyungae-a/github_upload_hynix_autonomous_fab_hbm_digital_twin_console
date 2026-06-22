from __future__ import annotations
import importlib.util, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
def main():
    total=0
    for p in sorted(Path(__file__).resolve().parent.glob("test_*.py")):
        spec=importlib.util.spec_from_file_location(p.stem,p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for name in dir(m):
            if name.startswith("test_") and callable(getattr(m,name)):
                getattr(m,name)(); total+=1
    print(f"PASS stdlib tests {total}")
if __name__=="__main__": main()
