PYTHON ?= python

.PHONY: setup setup-light setup-medium demo-light demo-medium demo-heavy run-canonical run-variants run-public-tools dashboard screenshots test validate validate-medium verify package-release verify-clean-unzip github-demo \
contract-check schema-check test-foundation test-memory-twin run-memory-twin test-circuit-twin run-ngspice test-rtl-proxy run-rtl-public-tools test-fab-twin run-fab-twin run-simpy test-factory-scene run-factory-scene test-coupling generate-evidence run-judges run-red-team-meta reveal-hidden-truth validate-docs verify-container-light verify-container-medium

setup:
	$(PYTHON) -B scripts/setup_repo.py

setup-light: setup

setup-medium: setup
	$(PYTHON) -B scripts/setup_repo.py --profile medium

demo-light:
	$(PYTHON) -B -m twin_core.scenario_runner demo-light

demo-medium:
	$(PYTHON) -B -m twin_core.scenario_runner demo-medium

demo-heavy:
	$(PYTHON) -B -m twin_core.scenario_runner demo-heavy

run-canonical:
	$(PYTHON) -B -m twin_core.scenario_runner run-canonical

run-variants:
	$(PYTHON) -B scenarios/generate_variants.py
	$(PYTHON) -B -m twin_core.scenario_runner run-variants

run-public-tools:
	$(PYTHON) -B -m twin_core.scenario_runner run-public-tools

dashboard:
	$(PYTHON) -B -m twin_core.scenario_runner dashboard

screenshots:
	$(PYTHON) -B scripts/generate_screenshots.py

test:
	$(PYTHON) -B tests/run_tests.py

validate:
	$(PYTHON) -B validation/validate_real_run_counts.py
	$(PYTHON) -B validation/validate_no_all_mock_release.py
	$(PYTHON) -B validation/validate_engine_computed_evidence.py
	$(PYTHON) -B validation/validate_public_tool_receipts.py
	$(PYTHON) -B validation/validate_ai_judges_not_scripted.py
	$(PYTHON) -B validation/validate_judge_sensitivity.py
	$(PYTHON) -B validation/validate_red_team_partial_miss.py
	$(PYTHON) -B validation/validate_hidden_truth_isolation.py
	$(PYTHON) -B validation/validate_supervisor_non_overclaim.py
	$(PYTHON) -B validation/validate_scenario_question_coverage.py
	$(PYTHON) -B validation/validate_variant_suite.py
	$(PYTHON) -B validation/validate_dashboard_contract.py
	$(PYTHON) -B validation/validate_release_hygiene.py
	$(PYTHON) -B validation/validate_github_screenshots.py
	$(PYTHON) -B validation/validate_negative_fixtures.py
	$(PYTHON) -B validation/validate_metric_lineage.py
	$(PYTHON) -B validation/validate_fab_event_timeline.py
	$(PYTHON) -B validation/validate_factory_scene_contract.py
	$(PYTHON) -B validation/validate_variant_engine_receipts.py
	$(PYTHON) -B validation/validate_meta_judge_scope.py
	$(PYTHON) -B validation/validate_audit_metrics.py
	$(PYTHON) -B validation/validate_hynix_alignment_claims.py
	$(PYTHON) -B validation/validate_readme_depth.py
	$(PYTHON) -B validation/validate_ci_contract.py

validate-medium: validate
	$(PYTHON) -B validation/validate_v5_4_acceptance.py

verify:
	$(PYTHON) -B validation/validate_v5_4_acceptance.py

package-release:
	$(PYTHON) -B validation/package_release.py --package

verify-clean-unzip:
	$(PYTHON) -B validation/package_release.py --verify-clean-unzip

contract-check schema-check test-foundation:
	$(PYTHON) -B validation/validate_contract_lock.py

test-memory-twin run-memory-twin test-circuit-twin test-rtl-proxy test-fab-twin run-fab-twin test-factory-scene run-factory-scene test-coupling:
	$(PYTHON) -B tests/run_tests.py

run-ngspice:
	$(PYTHON) -B public_tool_runs/ngspice/run_ngspice.py

run-rtl-public-tools:
	$(PYTHON) -B public_tool_runs/rtl/run_yosys_synth.py
	$(PYTHON) -B public_tool_runs/rtl/run_verilator_lint.py

run-simpy:
	$(PYTHON) -B public_tool_runs/simpy/run_simpy_fab.py

generate-evidence:
	$(PYTHON) -B -m twin_core.scenario_runner generate-evidence

run-judges:
	$(PYTHON) -B -m twin_core.scenario_runner run-judges

run-red-team-meta:
	$(PYTHON) -B -m twin_core.scenario_runner run-red-team-meta

reveal-hidden-truth:
	$(PYTHON) -B -m twin_core.scenario_runner reveal-hidden-truth

validate-docs:
	$(PYTHON) -B validation/validate_hynix_alignment_claims.py
	$(PYTHON) -B validation/validate_readme_depth.py

verify-container-light verify-container-medium:
	$(PYTHON) -B validation/validate_ci_contract.py

github-demo: setup-light demo-light validate dashboard screenshots
