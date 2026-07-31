from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .expressions import Expr, TruthAssignment
from .truth_table import generate_assignments


@dataclass(frozen=True)
class ValidityResult:
    """The result of checking whether an argument is valid."""

    is_valid: bool
    counterexample: TruthAssignment | None = None


def check_validity(
    premises: Iterable[Expr],
    conclusion: Expr,
) -> ValidityResult:
    """Check whether the premises logically entail the conclusion."""

    premise_list = tuple(premises)

    if not isinstance(conclusion, Expr):
        raise TypeError("The conclusion must be a logical expression.")

    if any(not isinstance(premise, Expr) for premise in premise_list):
        raise TypeError("Every premise must be a logical expression.")

    variable_names = set(conclusion.variables())

    for premise in premise_list:
        variable_names |= premise.variables()

    for assignment in generate_assignments(variable_names):
        premises_are_true = all(
            premise.evaluate(assignment)
            for premise in premise_list
        )

        conclusion_is_false = not conclusion.evaluate(assignment)

        if premises_are_true and conclusion_is_false:
            return ValidityResult(
                is_valid=False,
                counterexample=assignment,
            )

    return ValidityResult(is_valid=True)
