from twin_core.io_utils import canonical_scenarios
from twin_core.fab_operation.discrete_event_engine import run_fab_operation
def test_fab_timeline():
 r=run_fab_operation(canonical_scenarios()[2]); assert len(r['raw']['event_timeline'])>10
