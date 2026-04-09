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

## patch-upstream-pr-6750 - Carried patch: show home path and model in gateway /status

Status: active
Scope: intended-for-upstream
Upstream: PR #6750 — `feat(gateway): show home path and model in /status`
Reason:
- Makes gateway `/status` show which Hermes home/profile the session is actually using.
- Surfaces the session's current model/provider without making users infer it from config or logs.

Files:
- `gateway/run.py`
- `tests/gateway/test_status_command.py`

Notes:
- Drop this carried patch once PR #6750 lands upstream and local `main` rebases onto that commit.
- Title display already landed upstream via PR #5942; this carry adds the missing path + model visibility.
- PR #4678 overlaps on model display but still does not add the path line.
