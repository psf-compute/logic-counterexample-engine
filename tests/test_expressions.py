import pytest

from logic_counterexample_engine import (
    Biconditional,
    Conjunction,
    Disjunction,
    Implication,
    Negation,
    Var,
)


def test_variable_evaluation() -> None:
    a = Var("A")

    assert a.evaluate({"A": True}) is True
    assert a.evaluate({"A": False}) is False


def test_missing_variable_raises_error() -> None:
    a = Var("A")

    with pytest.raises(KeyError):
        a.evaluate({})


def test_negation() -> None:
    a = Var("A")
    expression = Negation(a)

    assert expression.evaluate({"A": True}) is False
    assert expression.evaluate({"A": False}) is True


def test_conjunction() -> None:
    a = Var("A")
    b = Var("B")
    expression = Conjunction(a, b)

    assert expression.evaluate({"A": True, "B": True}) is True
    assert expression.evaluate({"A": True, "B": False}) is False


def test_disjunction() -> None:
    a = Var("A")
    b = Var("B")
    expression = Disjunction(a, b)

    assert expression.evaluate({"A": False, "B": False}) is False
    assert expression.evaluate({"A": False, "B": True}) is True


def test_implication() -> None:
    a = Var("A")
    b = Var("B")
    expression = Implication(a, b)

    assert expression.evaluate({"A": True, "B": False}) is False
    assert expression.evaluate({"A": False, "B": False}) is True


def test_biconditional() -> None:
    a = Var("A")
    b = Var("B")
    expression = Biconditional(a, b)

    assert expression.evaluate({"A": True, "B": True}) is True
    assert expression.evaluate({"A": False, "B": False}) is True
    assert expression.evaluate({"A": True, "B": False}) is False


def test_expression_reports_its_variables() -> None:
    a = Var("A")
    b = Var("B")
    expression = Implication(Conjunction(a, b), Negation(a))

    assert expression.variables() == {"A", "B"}
