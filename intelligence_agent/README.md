# Intelligence Agent Pulse Guard

Built per the Governance + Event + Neural Pulse kernels, this agent is the reality observer that feeds XIRO with structured insight every 15 minutes.

## Kernel References
- **XIRO Governance Kernel** (`xiro_agentic_flow/agentic flow/# XIRO_GOVERNANCE_KERNEL.md.txt`, section `Intelligence Agent`) mandates a medium-cognition market observer that monitors hiring trends and reports observations without recommending strategy.
- **XIRO Event-Driven Cognitive Kernel** defines the event bus/state governor, so every output from this agent is packaged as an event that XiRO can consume.
- **XIRO Neural Pulse Kernel (NPK)** describes the 15-minute pulse; the intelligence agent writes a reality snapshot for each firing of that neuron.
- **Structural Drift Lock (SDL)** ensures the agent also checks tone/identity before emitting a signal.

## Responsibilities
1. Gather only approved structured sources:
   - Candidate/Client data from `memory/` and `docs/` (RIG inputs)
   - Hardware telemetry from Victus (via native probes)
   - Behavioral context from intelligence seeds stored in this folder.
2. Emit a pulse snapshot (`pulse_snapshot.json`) containing capability, feature, and trend metadata.
3. Flag trigger conditions for the operations agent to start conversations, keeping the RIG graph isolated.

Run `python intelligence_agent/pulse_capture.py` inside the kernel loop so XiRO sees the full reality picture.
