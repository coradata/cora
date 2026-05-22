from __future__ import annotations

import subprocess
import sys

import pytest

from cora_extractors import main


def test_main_help_exits_clean(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "cora-extract" in captured.out


def test_main_no_args_exits_clean() -> None:
    assert main([]) == 0


def test_console_script_help_exits_clean() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "cora_extractors", "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "cora-extract" in result.stdout
