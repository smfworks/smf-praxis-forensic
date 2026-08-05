"""SMF Praxis Forensic Engineering vertical — registration module.

This package is the private paid Forensic Engineering vertical build for
Praxis. It depends on the open-core ``smf-praxis`` base and registers the
forensic vertical's spec with the base's
:mod:`hybridagent.verticals.registry` on import.

No state regulates "forensic engineering" separately; it falls under
general PE licensing everywhere. The existing evidence/chain-of-custody/
data-classification/authz/sandbox substrate in the base covers all 13
states. This vertical is therefore persona-only: the forensic persona +
READ-only autonomous posture. No vertical-specific compliance modules.

Installation::

    pip install praxis-agent            # open-core base (public, MIT)
    pip install praxis-forensic         # this vertical (private, commercial)

Compliance mode: ``enforced``. READ autonomous only; SEND + DESTRUCTIVE
held for human approval. The Forensic Engineering persona carries
evidence-integrity + chain-of-custody guardrails.
"""

from __future__ import annotations

from .registration import register

__version__ = "0.2.0"

__all__ = ["__version__", "register"]

register()