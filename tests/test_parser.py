import pytest

from logic_counterexample_engine import (
    Biconditional,
    Conjunction,
    Disjunction,
    Implication,
    Negation,
    Var,
)
from logic_counterexample_engine.parser import parse_formula


def test_parse_variable() -> None:
    assert parse_formula("A") == Var("A")


def test_parse_negation() -> None:
    assert parse_formula("not A") == Negation(Var("A"))


def test_and_has_priority_over_or() -> None:
    expression = parse_formula("A or B and C")

    assert expression == Disjunction(
        Var("A"),
        Conjunction(Var("B"), Var("C")),
    )


def test_parentheses_override_priority() -> None:
    expression = parse_formula("(A or B) and C")

    assert expression == Conjunction(
        Disjunction(Var("A"), Var("B")),
        Var("C"),
    )


def test_implication_is_right_associative() -> None:
    expression = parse_formula("A -> B -> C")

    assert expression == Implication(
        Var("A"),
        Implication(Var("B"), Var("C")),
    )


def test_parse_biconditional() -> None:
    expression = parse_formula("A iff B")

    assert expression == Biconditional(
        Var("A"),
        Var("B"),
    )


def test_parse_unicode_formula() -> None:
    expression = parse_formula("¬A ∨ (B ↔ C)")

    assert expression == Disjunction(
        Negation(Var("A")),
        Biconditional(Var("B"), Var("C")),
    )


def test_empty_formula_raises_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        parse_formula("")


def test_missing_closing_parenthesis_raises_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        parse_formula("(A and B")


def test_extra_input_raises_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        parse_formula("A B")
