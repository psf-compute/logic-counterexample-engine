from __future__ import annotations

import argparse
from collections.abc import Sequence

from .argument import check_argument


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description=(
            "Check whether a propositional-logic argument is valid "
            "and display a counterexample when it is invalid."
        )
    )

    parser.add_argument(
        "-p",
        "--premise",
        action="append",
        default=[],
        help=(
            "A premise of the argument. "
            "Repeat this option for multiple premises."
        ),
    )

    parser.add_argument(
        "-c",
        "--conclusion",
        required=True,
        help="The conclusion of the argument.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface."""

    parser = build_parser()
    arguments = parser.parse_args(argv)

    try:
        result = check_argument(
            premises=arguments.premise,
            conclusion=arguments.conclusion,
        )
    except (SyntaxError, TypeError, ValueError) as error:
        parser.error(str(error))

    if result.is_valid:
        print("Valid argument.")
        return 0

    print("Invalid argument.")

    if result.counterexample is not None:
        print("Counterexample:")

        for variable, value in sorted(result.counterexample.items()):
            print(f"  {variable} = {value}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
