# 09 AI Judgment Audit Layer

## Purpose

The AI Judgment Audit Layer tests whether technical-looking claims remain bounded by evidence. It is a portfolio governance layer: evidence packet, AI Judge, Red-team, Meta Judge, Virtual Supervisor, and Hidden Truth are all visible as separate artifacts.

## Flow

The canonical sequence is:

1. Evidence Packet
2. AI Judge
3. Red-team
4. Meta Judge
5. Virtual Supervisor
6. Hidden Truth

Each stage reads only the allowed visible evidence for its role. Hidden-truth material is frozen until after pre-reveal hashes are written, so the judge and red-team cannot silently use post-reveal data.

## Engine Structure

Evidence packets are built from current-run twin outputs and public-tool receipts. Rule-based judges make evidence-sensitive decisions. Red-team challenges are expected to catch most, not all, weaknesses. Meta Judge checks visible-only scope. Virtual Supervisor blocks overclaims, especially real signoff or proprietary equivalence claims.

## Dashboard Mapping

The Audit page renders the full six-stage decision flow. It exposes caught/escaped outcomes, approved or bounded claims, blocked claims, and the repeated `requires_real_signoff` boundary.

## Evidence Paths

- Evidence packets: `outputs/evidence_packets/S*.json`
- AI judgments: `outputs/ai_judgments/S*.json`
- Red-team challenges: `outputs/red_team_challenges/S*.json`
- Meta Judge outputs: `outputs/meta_judge_outputs/S*.json`
- Supervisor logs: `outputs/supervisor_gate_logs/S*.json`
- Hidden truth reveals: `outputs/hidden_truth_reveals/S*.json`
- Screenshot: `screenshots/06_ai_judgment_audit_flow.png`

## Claim Boundary

This layer supports claims about auditability, bounded reasoning, and failure discovery. It does not make a human signoff claim and does not replace domain review by memory, circuit, fab, or product engineers.
