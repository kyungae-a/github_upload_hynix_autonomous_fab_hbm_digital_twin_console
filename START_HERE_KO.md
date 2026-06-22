# Codex 시작 안내 — v5.4 최종 제품화

## 사용할 파일

현재 v5.3 제품 저장소 루트에 이 workflow overlay를 병합한 뒤 Codex에서 해당 루트를 trusted project로 엽니다. 새 하위 제품 폴더를 만들지 않습니다.

## 시작 문장

```text
Read AGENTS.md and CODEX_HYNIX_V5_4_FINAL_PRODUCTIZATION_MASTER.md in full. Treat docs/reference/hynix_v5_4_final_productization_directive.md and config/v5_4_contract_lock.json as non-negotiable. Upgrade the current Hynix Autonomous Fab × HBM Digital Twin Console in place. Explicitly spawn the writer and independent reviewer named in each P00–P11 ticket. Directly fix the five v5.4 gaps: HBM Gbps/GB/s normalization, computed Factory route map, screenshot visual semantics, product-grade docs, and genuine GitHub medium public-tool evidence. Do not accept runtime self-certification, frontend fallback data, fake CI evidence, card/JSON-dump screenshots, shallow docs, or a local READY state. Continue until all local gates reach AWAITING_GITHUB_MEDIUM, then finalize only from a genuine GitHub medium run and set READY_FOR_GITHUB_REVIEW after all reviewers and clean-unzip verification pass.
```

## CLI

```bash
python scripts/validate_v5_4_workflow.py
python scripts/validate_v5_4_state.py
bash scripts/run_codex_v5_4.sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_codex_v5_4.ps1
```

Codex가 로컬 환경에서 모든 구현을 끝냈지만 실제 GitHub Actions run이 아직 없다면 `AWAITING_GITHUB_MEDIUM`이 정상입니다. CI URL이나 REAL tool receipt를 로컬에서 만들어 최종 상태를 우회하지 않습니다.
