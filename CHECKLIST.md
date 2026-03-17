# Kernel-Aligned Build Checklist

Tracked tasks derived from the system + agentic-flow kernels. Each item references verified evidence in the repo.

- [x] Scan and ingest all `system_kernels` docs (core, graph, neural, guardrails) ✔ `system_kernels/`
- [x] Configure the intelligence agent as a pure external-data collector (no reasoning) ✔ `intelligence_agent/pulse_capture.py`
- [x] Document intelligence agent responsibilities aligned with Governance kernel ✔ `intelligence_agent/README.md`
- [x] Build mechanical memory spine + sync scripts ✔ `scripts/local_memory_spine_agent.py`, `scripts/mech_memory_sync.py`
- [x] Implement Neural Pulse heartbeat (STATUS/BREADCRUMB/WINDOW/PAST/CORE/FUTURE) ✔ `intelligence_agent/pulse_snapshot.json`
- [x] Enforce SDL guardrail on every output ✔ `system_kernels/guardrails/SDL (STRUCTURAL DRIFT LOCK).txt`
- [x] Mirror ProQruit intelligence summary into docs & RIG per kernels ✔ `docs/` updates + Google Docs exported report
- [x] Connect operations agent (claw) to WhatsApp per Execution kernel ✔ logs in tmux capture and gateway status
- [x] Complete OSS intelligence agent references, ensuring no cross-agent communication ✔ `intelligence_agent` folder plus heartbeat logic
- [x] Commit changes to GitHub with kernel references before cloud build exit ✔ `git push` above
