"""Registration — wire the forensic vertical into the Praxis base registry."""

from __future__ import annotations

from hybridagent.broker import RiskClass
from hybridagent.verticals.registry import (
    VerticalSpec,
    register_vertical_spec,
)


_FORENSIC_SPEC = VerticalSpec(
    name="forensic",
    persona_keyword="forensic",
    compliance_mode="enforced",
    autonomous={RiskClass.READ},
    held={RiskClass.SEND, RiskClass.DESTRUCTIVE},
    version="0.1.0",
)


def register() -> None:
    """Register the forensic vertical with the Praxis base registry.

    Persona-only: no manual eval cases. The generic persona + posture
    cases are generated from the spec by the base.
    """

    register_vertical_spec(_FORENSIC_SPEC)