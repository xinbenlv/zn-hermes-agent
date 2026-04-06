# Carried Patch Queue

Local-only patches we intentionally carry in the `xinbenlv/hermes-agent` fork.

Rules:
- Keep this list ordered. Patch 0001 is the highest-priority carried patch.
- Every carried patch should say whether it is local-only or intended for upstream.
- `AGENTS.md` / local workflow guidance stays local-only unless explicitly approved otherwise.
- Upstream PRs must stay scoped; do not leak local policy/docs into them.

## 0001 - Local carried patch: AGENTS.md carried-patch policy

Status: active
Scope: local-only
Upstream: never include in NousResearch/hermes-agent PRs unless explicitly requested
Reason:
- Documents the carried-patches approach for this fork.
- Encodes local workflow rules that are specific to Victor's fork and should not be pushed upstream by default.

Files:
- `AGENTS.md`

Notes:
- This patch should remain the first entry in the queue.
- Any future local-only workflow guidance should be added after this entry, not before it.
