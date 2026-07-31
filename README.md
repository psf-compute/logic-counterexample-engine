# Logic Counterexample Engine

A Python propositional-logic engine that parses formulas, generates truth tables, checks argument validity, and finds counterexamples for invalid arguments.

## Features

- Parse formulas written in ordinary logical notation
- Propositional variables
- Negation
- Conjunction
- Disjunction
- Implication
- Biconditional
- Automatic truth-assignment generation
- Complete truth-table evaluation
- Argument-validity checking
- Counterexamples for invalid arguments
- Command-line interface
- Automated testing with GitHub Actions

## Supported notation

| Operation | Supported forms |
|---|---|
| Negation | `not A`, `~A`, `!A`, `¬A` |
| Conjunction | `A and B`, `A & B`, `A ∧ B` |
| Disjunction | `A or B`, `A \| B`, `A ∨ B` |
| Implication | `A implies B`, `A -> B`, `A → B` |
| Biconditional | `A iff B`, `A <-> B`, `A ↔ B` |

Parentheses may be used to control grouping:

```text
(A -> B) and A
```

## Python example

```python
from logic_counterexample_engine import check_argument

result = check_argument(
    premises=["A -> B", "B"],
    conclusion="A",
)

print(result.is_valid)
print(result.counterexample)
```

Output:

```text
False
{'A': False, 'B': True}
```

The counterexample shows that both premises can be true while the conclusion is false. Therefore, affirming the consequent is invalid.

## Command-line usage

Install the project from the repository directory:

```bash
python -m pip install -e .
```

Check a valid argument:

```bash
logic-counterexample \
  --premise "A -> B" \
  --premise "A" \
  --conclusion "B"
```

Output:

```text
Valid argument.
```

Check an invalid argument:

```bash
logic-counterexample \
  --premise "A -> B" \
  --premise "B" \
  --conclusion "A"
```

Output:

```text
Invalid argument.
Counterexample:
  A = False
  B = True
```

Repeat `--premise` for each premise in the argument.

## How validity is checked

An argument is valid when there is no truth assignment under which:

1. every premise is true; and
2. the conclusion is false.

The engine generates every possible assignment for the variables in the argument. If it finds an assignment satisfying both conditions, it returns that assignment as a counterexample.

## Development

Install the project and its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the tests:

```bash
pytest
```

GitHub Actions automatically installs the project and runs the test suite after every push and pull request.

## License

This project is available under the MIT License.
