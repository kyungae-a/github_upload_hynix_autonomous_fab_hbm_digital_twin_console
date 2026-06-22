from twin_core.io_utils import canonical_scenarios
from twin_core.factory_scene.scene_graph import run_factory_scene
def test_factory_graph():
 r=run_factory_scene(canonical_scenarios()[2]); assert r['parsed']['node_count']>=5
