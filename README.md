# Logic Counterexample Engine

A Python propositional-logic engine that evaluates logical expressions, generates truth tables, checks argument validity, and produces counterexamples for invalid arguments.

## Features

- Propositional variables
- Negation: `¬A`
- Conjunction: `A ∧ B`
- Disjunction: `A ∨ B`
- Implication: `A → B`
- Biconditional: `A ↔ B`
- Automatic truth-assignment generation
- Complete truth-table evaluation
- Argument-validity checking
- Counterexamples for invalid arguments
- Automated testing with GitHub Actions

## Example

```python
from logic_counterexample_engine import (
    Implication,
    Var,
    check_validity,
)

a = Var("A")
b = Var("B")

result = check_validity(
    premises=[
        Implication(a, b),
        b,
    ],
    conclusion=a,
)

print(result.is_valid)
print(result.counterexample)
```

Output:

```text
False
{'A': False, 'B': True}
```

The counterexample shows that the premises can both be true while the conclusion is false. Therefore, affirming the consequent is invalid.

## Validity

An argument is valid when there is no truth assignment under which:

1. every premise is true; and
2. the conclusion is false.

The engine checks every possible assignment. If it finds such a case, it returns that assignment as a counterexample.

## Development

Install the project and its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the tests:

```bash
pytest
```

GitHub Actions also runs the test suite automatically after every push and pull request.

## Current limitation

Logical expressions must currently be constructed with Python classes. A text parser and command-line interface are planned so users can enter expressions such as:

```text
(A -> B) & A
```

## License

This project is available under the MIT License.
