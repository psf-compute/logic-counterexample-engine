from __future__ import annotations

from .expressions import (
    Biconditional,
    Conjunction,
    Disjunction,
    Expr,
    Implication,
    Negation,
    Var,
)
from .lexer import Token, TokenKind, tokenize


class Parser:
    """Convert logical-formula tokens into an expression tree."""

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.position = 0

    @property
    def current(self) -> Token:
        return self.tokens[self.position]

    @property
    def previous(self) -> Token:
        return self.tokens[self.position - 1]

    def advance(self) -> Token:
        token = self.current

        if token.kind is not TokenKind.EOF:
            self.position += 1

        return token

    def match(self, *kinds: TokenKind) -> bool:
        if self.current.kind in kinds:
            self.advance()
            return True

        return False

    def expect(self, kind: TokenKind, message: str) -> Token:
        if self.current.kind is kind:
            return self.advance()

        raise SyntaxError(
            f"{message} Found {self.current.value!r} "
            f"at position {self.current.position}."
        )

    def parse(self) -> Expr:
        if self.current.kind is TokenKind.EOF:
            raise SyntaxError("The formula cannot be empty.")

        expression = self.parse_biconditional()

        self.expect(
            TokenKind.EOF,
            "Expected the end of the formula.",
        )

        return expression

    def parse_biconditional(self) -> Expr:
        expression = self.parse_implication()

        while self.match(TokenKind.BICONDITIONAL):
            right = self.parse_implication()
            expression = Biconditional(expression, right)

        return expression

    def parse_implication(self) -> Expr:
        expression = self.parse_disjunction()

        if self.match(TokenKind.IMPLICATION):
            right = self.parse_implication()
            expression = Implication(expression, right)

        return expression

    def parse_disjunction(self) -> Expr:
        expression = self.parse_conjunction()

        while self.match(TokenKind.OR):
            right = self.parse_conjunction()
            expression = Disjunction(expression, right)

        return expression

    def parse_conjunction(self) -> Expr:
        expression = self.parse_negation()

        while self.match(TokenKind.AND):
            right = self.parse_negation()
            expression = Conjunction(expression, right)

        return expression

    def parse_negation(self) -> Expr:
        if self.match(TokenKind.NOT):
            return Negation(self.parse_negation())

        return self.parse_primary()

    def parse_primary(self) -> Expr:
        if self.match(TokenKind.IDENTIFIER):
            return Var(self.previous.value)

        if self.match(TokenKind.LEFT_PARENTHESIS):
            expression = self.parse_biconditional()

            self.expect(
                TokenKind.RIGHT_PARENTHESIS,
                "Expected a closing parenthesis.",
            )

            return expression

        raise SyntaxError(
            "Expected a variable, negation, or opening parenthesis "
            f"at position {self.current.position}."
        )


def parse_formula(text: str) -> Expr:
    """Parse a textual propositional-logic formula."""

    return Parser(tokenize(text)).parse()
