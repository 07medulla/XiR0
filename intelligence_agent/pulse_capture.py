#!/usr/bin/env python3
"""Capture the Intelligence Agent pulse per the system kernels."""
from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

BASE = Path(__file__).resolve().parent
MEMORY_DIR = BASE.parent / "memory"
SYSTEM_KERNELS = BASE.parent / "system_kernels"
PULSE_FILE = BASE / "pulse_snapshot.json"

CAMEL = re.compile(r"^(\w+):\s*(.*)$")


def read_memory_entries(limit: int = 3) -> List[str]:
    files = sorted(MEMORY_DIR.glob("2026-03-*.md"))
    if len(files) > 1:
        files = files[:-1]
    files = files[-limit:]
    lines = []
    for path in files:
        lines.append(f"--- {path.name} ---")
        lines.extend([line.strip() for line in path.read_text().splitlines() if line.strip()])
    return lines


def candidate_summary() -> Dict[str, int]:
    pipeline = BASE.parent / "candidate_pipeline.csv"
    if not pipeline.exists():
        return {"missing": 0}
    counts: Dict[str, int] = {}
    seen = set()
    for line in pipeline.read_text().splitlines()[1:]:
        parts = [p.strip().strip('"') for p in line.split(",")]
        if not parts:
            continue
        name = parts[0] if parts[0] else "Unknown"
        city = parts[1] if len(parts) > 1 and parts[1] else "Unknown"
        if name in seen:
            continue
        seen.add(name)
        counts[city] = counts.get(city, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: -item[1])[:5])


def hardware_health() -> Dict[str, str]:
    def _run(cmd: List[str]) -> str:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return result.stdout.strip()
    health = {
        "free": _run(["free", "-m"]),
        "uptime": _run(["uptime"]),
        "nvidia": _run(["nvidia-smi", "--query-gpu=temperature.gpu,utilization.gpu", "--format=csv,noheader"]) if subprocess.run(["which", "nvidia-smi"], capture_output=True).returncode == 0 else "nvidia-smi missing",
    }
    return health


def system_features() -> Dict[str, List[str]]:
    features = {}
    for doc in (SYSTEM_KERNELS / "core").glob("*.txt"):
        features.setdefault("core", []).append(doc.name)
    for doc in (SYSTEM_KERNELS / "graph").glob("*.txt"):
        features.setdefault("graph", []).append(doc.name)
    features["guardrail"] = [p.name for p in (SYSTEM_KERNELS / "guardrails").glob("*.txt")]
    return features


def build_pulse() -> Dict[str, object]:
    now = datetime.now(timezone.utc)
    return {
        "timestamp": now.isoformat(),
        "status": "OBSERVATION_ONLY",
        "breadcrumb": "Deep system sweep (SSD, C: drive, backup, Clawphone, cloud) confirmed.",
        "window": {
            "hardware": hardware_health(),
            "agents": ["operations", "intelligence", "RIG", "SDL guardrail"],
            "features": system_features(),
        },
        "past": read_memory_entries(2),
        "core": {
            "candidate_summary": candidate_summary(),
            "pulse_sources": [str(p.relative_to(BASE.parent)) for p in (BASE.parent / "system_kernels").rglob("*.txt")],
        },
        "future": ["Proactive intelligence triggers", "03:00 IST continuity refresh", "Monitor WhatsApp transport"],
    }


def main() -> None:
    pulse = build_pulse()
    PULSE_FILE.write_text(json.dumps(pulse, indent=2))
    print(f"Pulse written to {PULSE_FILE}")


if __name__ == "__main__":
    main()
