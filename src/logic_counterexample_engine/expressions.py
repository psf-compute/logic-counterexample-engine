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


@dataclass(frozen=True)
class Conjunction(Expr):
    """A conjunction of two expressions, such as A ∧ B."""

    left: Expr
    right: Expr

    def __post_init__(self) -> None:
        if not isinstance(self.left, Expr) or not isinstance(self.right, Expr):
            raise TypeError(
                "Conjunction requires two logical expressions."
            )

    def evaluate(self, assignment: TruthAssignment) -> bool:
        return (
            self.left.evaluate(assignment)
            and self.right.evaluate(assignment)
        )

    def variables(self) -> set[str]:
        return self.left.variables() | self.right.variables()

    def __str__(self) -> str:
        return f"({self.left} ∧ {self.right})"



@dataclass(frozen=True)
class Disjunction(Expr):
    """A disjunction of two expressions, such as A ∨ B."""

    left: Expr
    right: Expr

    def __post_init__(self) -> None:
        if not isinstance(self.left, Expr) or not isinstance(self.right, Expr):
            raise TypeError(
                "Disjunction requires two logical expressions."
            )

    def evaluate(self, assignment: TruthAssignment) -> bool:
        return (
            self.left.evaluate(assignment)
            or self.right.evaluate(assignment)
        )

    def variables(self) -> set[str]:
        return self.left.variables() | self.right.variables()

    def __str__(self) -> str:
        return f"({self.left} ∨ {self.right})"


@dataclass(frozen=True)
class Implication(Expr):
    """An implication of two expressions, such as A → B."""

    antecedent: Expr
    consequent: Expr

    def __post_init__(self) -> None:
        if (
            not isinstance(self.antecedent, Expr)
            or not isinstance(self.consequent, Expr)
        ):
            raise TypeError(
                "Implication requires two logical expressions."
            )

    def evaluate(self, assignment: TruthAssignment) -> bool:
        return (
            not self.antecedent.evaluate(assignment)
            or self.consequent.evaluate(assignment)
        )

    def variables(self) -> set[str]:
        return (
            self.antecedent.variables()
            | self.consequent.variables()
        )

    def __str__(self) -> str:
        return f"({self.antecedent} → {self.consequent})"


@dataclass(frozen=True)
class Biconditional(Expr):
    """A biconditional between two expressions, such as A ↔ B."""

    left: Expr
    right: Expr

    def __post_init__(self) -> None:
        if not isinstance(self.left, Expr) or not isinstance(self.right, Expr):
            raise TypeError(
                "Biconditional requires two logical expressions."
            )

    def evaluate(self, assignment: TruthAssignment) -> bool:
        return (
            self.left.evaluate(assignment)
            == self.right.evaluate(assignment)
        )

    def variables(self) -> set[str]:
        return self.left.variables() | self.right.variables()

    def __str__(self) -> str:
        return f"({self.left} ↔ {self.right})"
