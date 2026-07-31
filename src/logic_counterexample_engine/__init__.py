"""Tools for evaluating propositional logic and checking arguments."""
from .argument import check_argument
from .expressions import (
    Biconditional,
    Conjunction,
    Disjunction,
    Expr,
    Implication,
    Negation,
    TruthAssignment,
    Var,
)

from .parser import parse_formula

from .truth_table import build_truth_table, generate_assignments
from .validity import ValidityResult, check_validity

__all__ = [
    "Biconditional",
    "Conjunction",
    "Disjunction",
    "Expr",
    "Implication",
    "Negation",
    "TruthAssignment",
    "Var",
    "ValidityResult",
    "build_truth_table",
    "check_validity",
    "generate_assignments",
    "parse_formula",
    "check_argument",
]
