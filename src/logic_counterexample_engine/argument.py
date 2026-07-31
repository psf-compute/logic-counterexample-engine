from __future__ import annotations

from collections.abc import Iterable

from .parser import parse_formula
from .validity import ValidityResult, check_validity


def check_argument(
    premises: Iterable[str],
    conclusion: str,
) -> ValidityResult:
    """Check an argument written as textual logical formulas."""

    if isinstance(premises, (str, bytes)):
        raise TypeError(
            "Premises must be a collection of formula strings, "
            "not one string."
        )

    if not isinstance(conclusion, str):
        raise TypeError("The conclusion must be a formula string.")

    premise_texts = tuple(premises)

    if any(not isinstance(premise, str) for premise in premise_texts):
        raise TypeError("Every premise must be a formula string.")

    parsed_premises = [
        parse_formula(premise)
        for premise in premise_texts
    ]
    parsed_conclusion = parse_formula(conclusion)

    return check_validity(
        premises=parsed_premises,
        conclusion=parsed_conclusion,
    )
