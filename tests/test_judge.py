from twin_core.io_utils import read_json, ROOT
from agents.rule_based_judges import decide, perturb
def test_judge_sensitivity_after_demo():
 ps=list((ROOT/'outputs'/'evidence_packets').glob('S*.json'))
 if ps: assert sum(decide(read_json(p))['decision'] != decide(perturb(read_json(p)))['decision'] for p in ps) >= 5
