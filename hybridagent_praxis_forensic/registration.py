"""Registration — wire the forensic vertical into the Praxis base registry."""

from __future__ import annotations

from pathlib import Path

from hybridagent.broker import RiskClass
from hybridagent.verticals.registry import (
    VerticalSpec,
    register_vertical_pack_root,
    register_vertical_spec,
)

_FORENSIC_SPEC = VerticalSpec(
    name="forensic",
    persona_keyword="forensic",
    compliance_mode="enforced",
    autonomous={RiskClass.READ},
    held={RiskClass.SEND, RiskClass.DESTRUCTIVE},
    version="0.1.2",
)


def register() -> None:
    """Register the forensic vertical with the Praxis base registry.

    The pack contributes no manual eval cases; the generic persona + posture
    cases are generated from the spec by the base.
    """

    register_vertical_spec(_FORENSIC_SPEC)
    register_vertical_pack_root(Path(__file__).resolve().parent / "packs")