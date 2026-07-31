from logic_counterexample_engine import (
    Conjunction,
    Var,
    build_truth_table,
    generate_assignments,
)


def test_generate_assignments_for_two_variables() -> None:
    assignments = list(generate_assignments({"A", "B"}))

    assert assignments == [
        {"A": False, "B": False},
        {"A": False, "B": True},
        {"A": True, "B": False},
        {"A": True, "B": True},
    ]


def test_build_truth_table_for_conjunction() -> None:
    a = Var("A")
    b = Var("B")
    expression = Conjunction(a, b)

    table = build_truth_table(expression)

    assert table == [
        ({"A": False, "B": False}, False),
        ({"A": False, "B": True}, False),
        ({"A": True, "B": False}, False),
        ({"A": True, "B": True}, True),
    ]
