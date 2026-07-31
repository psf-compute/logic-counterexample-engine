import pytest

from logic_counterexample_engine.argument import check_argument


def test_text_based_modus_ponens_is_valid() -> None:
    result = check_argument(
        premises=["A -> B", "A"],
        conclusion="B",
    )

    assert result.is_valid is True
    assert result.counterexample is None


def test_text_based_affirming_the_consequent_is_invalid() -> None:
    result = check_argument(
        premises=["A -> B", "B"],
        conclusion="A",
    )

    assert result.is_valid is False
    assert result.counterexample == {
        "A": False,
        "B": True,
    }


def test_premises_cannot_be_one_string() -> None:
    with pytest.raises(TypeError):
        check_argument(
            premises="A -> B",
            conclusion="B",
        )


def test_every_premise_must_be_a_string() -> None:
    with pytest.raises(TypeError):
        check_argument(
            premises=["A", 123],
            conclusion="B",
        )


def test_conclusion_must_be_a_string() -> None:
    with pytest.raises(TypeError):
        check_argument(
            premises=["A"],
            conclusion=123,
        )
