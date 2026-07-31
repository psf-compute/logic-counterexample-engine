from logic_counterexample_engine import Implication, Var, check_validity


def test_modus_ponens_is_valid() -> None:
    a = Var("A")
    b = Var("B")

    result = check_validity(
        premises=[Implication(a, b), a],
        conclusion=b,
    )

    assert result.is_valid is True
    assert result.counterexample is None


def test_affirming_the_consequent_is_invalid() -> None:
    a = Var("A")
    b = Var("B")

    result = check_validity(
        premises=[Implication(a, b), b],
        conclusion=a,
    )

    assert result.is_valid is False
    assert result.counterexample == {
        "A": False,
        "B": True,
    }
