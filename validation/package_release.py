import argparse
from v5_checks import package_release, verify_clean_unzip, verify_release_payload
p=argparse.ArgumentParser(); p.add_argument('--package',action='store_true'); p.add_argument('--verify-clean-unzip',action='store_true'); a=p.parse_args()
package_release() if a.package else (verify_clean_unzip() if a.verify_clean_unzip else verify_release_payload())
