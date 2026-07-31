import pytest

from logic_counterexample_engine.lexer import (
    TokenKind,
    tokenize,
)


def test_tokenize_symbolic_formula() -> None:
    tokens = tokenize("(A -> B) & A")

    assert [token.kind for token in tokens] == [
        TokenKind.LEFT_PARENTHESIS,
        TokenKind.IDENTIFIER,
        TokenKind.IMPLICATION,
        TokenKind.IDENTIFIER,
        TokenKind.RIGHT_PARENTHESIS,
        TokenKind.AND,
        TokenKind.IDENTIFIER,
        TokenKind.EOF,
    ]

    assert [token.value for token in tokens] == [
        "(",
        "A",
        "->",
        "B",
        ")",
        "&",
        "A",
        "",
    ]


def test_tokenize_word_operators() -> None:
    tokens = tokenize("not Rain or Wet")

    assert [token.kind for token in tokens] == [
        TokenKind.NOT,
        TokenKind.IDENTIFIER,
        TokenKind.OR,
        TokenKind.IDENTIFIER,
        TokenKind.EOF,
    ]


def test_tokenize_unicode_operators() -> None:
    tokens = tokenize("¬A ∨ (B ↔ C)")

    assert [token.kind for token in tokens] == [
        TokenKind.NOT,
        TokenKind.IDENTIFIER,
        TokenKind.OR,
        TokenKind.LEFT_PARENTHESIS,
        TokenKind.IDENTIFIER,
        TokenKind.BICONDITIONAL,
        TokenKind.IDENTIFIER,
        TokenKind.RIGHT_PARENTHESIS,
        TokenKind.EOF,
    ]


def test_keywords_are_case_insensitive() -> None:
    tokens = tokenize("A AND B")

    assert tokens[1].kind is TokenKind.AND


def test_identifier_may_contain_numbers_and_underscores() -> None:
    tokens = tokenize("Premise_1")

    assert tokens[0].kind is TokenKind.IDENTIFIER
    assert tokens[0].value == "Premise_1"


def test_unexpected_character_raises_syntax_error() -> None:
    with pytest.raises(SyntaxError):
        tokenize("A + B")


def test_non_string_input_raises_type_error() -> None:
    with pytest.raises(TypeError):
        tokenize(123)  # type: ignore[arg-type]
