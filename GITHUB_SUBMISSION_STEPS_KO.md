# GitHub 제출 및 v5.4 READY 전환 절차

이 저장소의 로컬 상태는 `AWAITING_GITHUB_MEDIUM`입니다. 이는 실패가 아니라 v5.4 계약상 정직한 상태입니다. 실제 `READY_FOR_GITHUB_REVIEW`는 GitHub Actions `medium` workflow가 같은 commit에서 실행되고, 네 public tool 증거가 실제 run으로 기록된 뒤에만 설정됩니다.

## 1. 업로드할 패키지

현재 제출용 repo ZIP:

`release/hynix-autonomous-fab-hbm-digital-twin-console.zip`

이 ZIP을 새 폴더에 풀고, 그 폴더 내용을 GitHub repository root로 올리면 됩니다. ZIP 내부에는 `.github/workflows/medium.yml`, `scripts/generate_ci_run_manifest.py`, `scripts/finalize_v5_4_github_medium.py`, v5.4 validators, frontend, screenshots, docs, outputs가 포함됩니다.

## 2. GitHub에서 일어나는 일

`medium` workflow는 다음 순서로 동작합니다.

1. Ubuntu runner에서 Python 3.12 준비
2. `ngspice`, `yosys`, `verilator` 설치
3. `simpy` Python package 설치
4. `make setup-medium demo-medium run-public-tools`
5. `scripts/generate_ci_run_manifest.py`
6. `scripts/finalize_v5_4_github_medium.py`
7. `make dashboard screenshots validate validate-medium package-release verify-clean-unzip`
8. `hynix-v5-4-medium-evidence` artifact 업로드

## 3. 성공 기준

GitHub Actions run이 성공하면 artifact 안에 다음이 있어야 합니다.

- `outputs/public_tool_evidence/ci_run_manifest.json`
- `outputs/public_tool_receipts/ngspice.json`
- `outputs/public_tool_receipts/yosys.json`
- `outputs/public_tool_receipts/verilator.json`
- `outputs/public_tool_receipts/simpy.json`
- `docs/v5_4_build_state.json`
- `release/hynix-autonomous-fab-hbm-digital-twin-console.zip`
- `release/hynix-autonomous-fab-hbm-digital-twin-console.release_manifest.json`

`docs/v5_4_build_state.json`은 GitHub run 이후 다음 상태여야 합니다.

```json
{
  "status": "READY_FOR_GITHUB_REVIEW",
  "current_phase": "P11"
}
```

`ci_medium_evidence`에는 실제 `github_run_url`, `commit_sha`, 그리고 네 tool status가 기록되어야 합니다. 이 값은 로컬에서 만들어 넣으면 안 됩니다.

## 4. 로컬에서 다시 확인하는 명령

GitHub artifact를 내려받아 풀었다면, repo root에서 다음을 실행합니다.

```powershell
python -B scripts/verify_github_medium_artifact.py --artifact .
python -B validation/validate_v5_4_acceptance.py
python -B validation/package_release.py --verify-clean-unzip
```

MSYS2 make를 쓰는 환경이라면 다음도 가능합니다.

```powershell
C:\msys64\usr\bin\make.exe verify-clean-unzip PYTHON="C:/Users/qkswk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe"
```

다운로드한 GitHub artifact가 ZIP 파일이라면 다음처럼 직접 검사할 수 있습니다.

```powershell
python -B scripts/verify_github_medium_artifact.py --artifact C:\path\to\hynix-v5-4-medium-evidence.zip
```

## 5. Claim Boundary

이 프로젝트는 public-model portfolio evidence입니다. GitHub medium 성공은 재현 가능한 공개 도구 실행과 evidence chain을 증명합니다. 실제 SK hynix 내부 접근, 제품 signoff, 생산 fab control, 상업용 HBM/DRAM 설계 검증을 주장하지 않습니다.
