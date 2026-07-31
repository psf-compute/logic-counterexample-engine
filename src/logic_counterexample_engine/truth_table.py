from __future__ import annotations

from itertools import product
from typing import Iterable, Iterator

from .expressions import Expr, TruthAssignment


def generate_assignments(
    variable_names: Iterable[str],
) -> Iterator[dict[str, bool]]:
    """Generate every truth assignment for the given variables."""

    names = sorted(set(variable_names))

    for values in product((False, True), repeat=len(names)):
        yield dict(zip(names, values))


def build_truth_table(
    expression: Expr,
) -> list[tuple[TruthAssignment, bool]]:
    """Evaluate an expression under every possible truth assignment."""

    return [
        (assignment, expression.evaluate(assignment))
        for assignment in generate_assignments(expression.variables())
    ]
