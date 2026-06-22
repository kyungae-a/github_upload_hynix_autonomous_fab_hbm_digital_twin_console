from twin_core.io_utils import canonical_scenarios
from twin_core.memory_system.hbm_workload_engine import run_memory_system
def test_memory_run():
 r=run_memory_system(canonical_scenarios()[0]); assert r['receipt']['status']=='REAL_INTERNAL_RUN'; assert r['parsed']['sustained_bandwidth_gbps']>0
