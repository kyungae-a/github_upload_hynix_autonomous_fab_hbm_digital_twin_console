# 13 Interview Talking Points KO

## 30초 설명

이 프로젝트는 HBM 워크로드, 회로/물리 proxy, Fab Q-time 흐름, 공장 routing, AI 판단 감사 흐름을 하나의 public-model Digital Twin 콘솔로 연결한 포트폴리오입니다. 실제 제품 signoff나 내부 데이터 접근을 주장하지 않고, 공개 지식 기반의 실행 가능한 모델과 검증 가능한 evidence chain을 보여주는 데 초점을 맞췄습니다.

## 1분 설명

핵심은 단일 성능 지표가 아니라 의사결정 경계입니다. HBM에서는 순간 bandwidth가 좋아도 thermal pressure, refresh overhead, turnaround loss 때문에 sustained bandwidth가 달라집니다. Fab에서는 LOT priority가 높아도 downstream Q-time을 깨뜨릴 수 있습니다. AI judge는 visible metric으로 판단하고, red-team은 그 판단의 빈틈을 찾고, virtual supervisor는 실제 signoff가 필요한 claim을 차단합니다.

## 3분 설명

제가 보여주고 싶은 것은 "AI를 반도체 설계/제조 의사결정에 어떻게 안전하게 붙일 수 있는가"입니다. 그래서 HBM memory twin, circuit/physical proxy twin, Fab operation twin, factory routing twin을 따로 만든 뒤, scenario evidence packet으로 묶었습니다. 각 scenario는 engine output, public-tool receipt, metric lineage, AI judgment, red-team, supervisor gate, hidden truth reveal까지 이어집니다.

이 구조는 Hynix의 Autonomous Fab, HBM, Digital Twin 방향과 맞닿아 있습니다. 다만 저는 proprietary data나 real signoff를 가진 사람이 아니기 때문에, 프로젝트 전체는 public-model only로 제한했습니다. 그 대신 제한을 숨기지 않고 증거와 claim boundary를 분리했습니다.

## 왜 실제 signoff가 아닌가

실제 signoff는 PDK, 측정 데이터, tool-qualified flow, domain engineer review, product context가 필요합니다. 이 repo는 그런 권한을 주장하지 않습니다. 대신 proxy execution pass, proxy design pass, real signoff allowed를 분리해 표현합니다.

## AI를 어떻게 쓰는가

AI judge는 visible metrics만 읽습니다. Red-team은 judge가 놓칠 수 있는 boundary를 찾습니다. Meta judge는 red-team 결과를 정리합니다. Virtual supervisor는 claim을 public-model evidence 수준으로 제한합니다. Hidden truth reveal은 AI 판단이 왜 plausible but incomplete일 수 있는지 보여줍니다.

## Hynix 연결 포인트

- HBM: bandwidth, latency, thermal pressure, refresh, turnaround
- Autonomous Fab: LOT priority, Q-time, downstream bottleneck
- Digital Twin: factory scene, route congestion, dashboard evidence explorer
- AI governance: judge, red-team, supervisor claim boundary

## 면접에서 강조할 문장

"저는 단순히 AI가 정답을 낸다고 주장하지 않고, AI 판단이 어떤 evidence를 보고 어떤 boundary에서 멈춰야 하는지까지 구현했습니다. 반도체 설계와 제조에서는 성능보다 hard constraint와 signoff boundary가 먼저라는 점을 포트폴리오 구조 안에 넣었습니다."
