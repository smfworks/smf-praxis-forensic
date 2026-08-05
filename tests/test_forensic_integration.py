"""Forensic vertical registration, authority, and governance posture."""
from hybridagent.broker import GovernanceBroker, GovernancePolicy, RiskClass, Verdict
from hybridagent.pack import apply_to_policy, load_pack
from hybridagent.vertical_evals import vertical_eval_cases
from hybridagent.verticals.registry import get_vertical_spec

import hybridagent_praxis_forensic  # noqa: F401
from hybridagent_praxis_forensic.personas.forensic_engineering.authority import policy


def test_forensic_registers_and_generic_evals_pass():
    spec = get_vertical_spec("forensic")
    assert spec is not None
    assert spec.version == "0.2.0"
    cases = [case for case in vertical_eval_cases() if case.id.startswith("vertical.forensic.")]
    assert {case.id for case in cases} == {
        "vertical.forensic.persona",
        "vertical.forensic.posture",
    }
    assert all(case.evaluate().passed for case in cases)


def test_forensic_authority_and_read_only_posture():
    authority = policy("NY")
    assert authority.vertical == "forensic_engineering"
    assert authority.jurisdiction == "NY"

    vertical_pack = load_pack("forensic")
    assert vertical_pack.version == "0.2.0"
    assert vertical_pack.path is not None
    governance = GovernancePolicy(allowed_tools={"read_file"})
    apply_to_policy(vertical_pack, governance)
    broker = GovernanceBroker(governance)
    assert broker.authorize("agent", "read_file", RiskClass.READ, {}).verdict is Verdict.ALLOW
    assert (
        broker.authorize("agent", "read_file", RiskClass.SEND, {}).verdict
        is Verdict.NEEDS_APPROVAL
    )