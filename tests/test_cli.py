import pytest

from logic_counterexample_engine.cli import main


def test_cli_reports_valid_argument(capsys: pytest.CaptureFixture[str]) -> None:
    exit_code = main(
        [
            "--premise",
            "A -> B",
            "--premise",
            "A",
            "--conclusion",
            "B",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "Valid argument.\n"
    assert captured.err == ""


def test_cli_reports_invalid_argument(
    capsys: pytest.CaptureFixture[str],
) -> None:
    exit_code = main(
        [
            "--premise",
            "A -> B",
            "--premise",
            "B",
            "--conclusion",
            "A",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 1
    assert captured.out == (
        "Invalid argument.\n"
        "Counterexample:\n"
        "  A = False\n"
        "  B = True\n"
    )
    assert captured.err == ""


def test_cli_reports_formula_errors(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as error:
        main(
            [
                "--premise",
                "A ->",
                "--conclusion",
                "B",
            ]
        )

    captured = capsys.readouterr()

    assert error.value.code == 2
    assert "error:" in captured.err
