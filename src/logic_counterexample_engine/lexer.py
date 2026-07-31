from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class TokenKind(Enum):
    """The kinds of tokens allowed in a logical formula."""

    IDENTIFIER = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    IMPLICATION = auto()
    BICONDITIONAL = auto()
    LEFT_PARENTHESIS = auto()
    RIGHT_PARENTHESIS = auto()
    EOF = auto()


@dataclass(frozen=True)
class Token:
    """One meaningful piece of a logical formula."""

    kind: TokenKind
    value: str
    position: int


_KEYWORDS = {
    "not": TokenKind.NOT,
    "and": TokenKind.AND,
    "or": TokenKind.OR,
    "implies": TokenKind.IMPLICATION,
    "iff": TokenKind.BICONDITIONAL,
}


_SYMBOLS = (
    ("<->", TokenKind.BICONDITIONAL),
    ("->", TokenKind.IMPLICATION),
    ("¬", TokenKind.NOT),
    ("~", TokenKind.NOT),
    ("!", TokenKind.NOT),
    ("∧", TokenKind.AND),
    ("&", TokenKind.AND),
    ("∨", TokenKind.OR),
    ("|", TokenKind.OR),
    ("→", TokenKind.IMPLICATION),
    ("↔", TokenKind.BICONDITIONAL),
    ("(", TokenKind.LEFT_PARENTHESIS),
    (")", TokenKind.RIGHT_PARENTHESIS),
)


def tokenize(text: str) -> list[Token]:
    """Convert a logical formula into a sequence of tokens."""

    if not isinstance(text, str):
        raise TypeError("The formula must be a string.")

    tokens: list[Token] = []
    position = 0

    while position < len(text):
        character = text[position]

        if character.isspace():
            position += 1
            continue

        if character.isalpha() or character == "_":
            start = position
            position += 1

            while position < len(text):
                current = text[position]

                if not (current.isalnum() or current == "_"):
                    break

                position += 1

            value = text[start:position]
            kind = _KEYWORDS.get(
                value.lower(),
                TokenKind.IDENTIFIER,
            )

            tokens.append(Token(kind, value, start))
            continue

        for symbol, kind in _SYMBOLS:
            if text.startswith(symbol, position):
                tokens.append(Token(kind, symbol, position))
                position += len(symbol)
                break
        else:
            raise SyntaxError(
                f"Unexpected character {character!r} "
                f"at position {position}."
            )

    tokens.append(Token(TokenKind.EOF, "", len(text)))
    return tokens
