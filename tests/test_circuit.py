from twin_core.io_utils import canonical_scenarios
from twin_core.circuit_physical.read_path_model import run_circuit_physical
def test_no_real_signoff():
 r=run_circuit_physical(canonical_scenarios()[-1]); assert r['parsed']['real_signoff_claim_allowed'] is False
