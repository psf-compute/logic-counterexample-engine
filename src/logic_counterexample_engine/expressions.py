from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Mapping


TruthAssignment = Mapping[str, bool]


class Expr(ABC):
    """Base class for every propositional-logic expression."""

    @abstractmethod
    def evaluate(self, assignment: TruthAssignment) -> bool:
        """Evaluate the expression under a truth-value assignment."""
        raise NotImplementedError

    @abstractmethod
    def variables(self) -> set[str]:
        """Return the variable names used in the expression."""
        raise NotImplementedError


@dataclass(frozen=True)
class Var(Expr):
    """A propositional variable such as A, P1, or Rain."""

    name: str

    def __post_init__(self) -> None:
        if not self.name or not self.name.isidentifier():
            raise ValueError(
                "Variable names must be valid identifiers, "
                "such as A, P1, or Rain."
            )

    def evaluate(self, assignment: TruthAssignment) -> bool:
        if self.name not in assignment:
            raise KeyError(
                f"Missing truth value for variable '{self.name}'."
            )

        value = assignment[self.name]

        if not isinstance(value, bool):
            raise TypeError(
                f"Truth value for '{self.name}' must be True or False."
            )

        return value

    def variables(self) -> set[str]:
        return {self.name}

    def __str__(self) -> str:
        return self.name


@dataclass(frozen=True)
class Negation(Expr):
    """The negation of an expression, such as ¬A."""

    operand: Expr

    def __post_init__(self) -> None:
        if not isinstance(self.operand, Expr):
            raise TypeError("Negation requires a logical expression.")

    def evaluate(self, assignment: TruthAssignment) -> bool:
        return not self.operand.evaluate(assignment)

    def variables(self) -> set[str]:
        return self.operand.variables()

    def __str__(self) -> str:
        return f"¬{self.operand}"

