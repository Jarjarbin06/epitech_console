import pytest
import time
import io


from epitech_console.System.console import Console


def test_console_print_basic(
        capsys
    ) -> None:
    buffer = io.StringIO()
    Console.print("hello", file=buffer)
    out = capsys.readouterr().out
    assert out == "hello\n"


def test_console_print_with_start_end(
        capsys
    ) -> None:
    buffer = io.StringIO()
    Console.print("world", start=">>> ", end=" !!!\n", file=buffer)
    out = capsys.readouterr().out
    assert out == ">>> world !!!\n"


def test_console_print_with_sleep(
        monkeypatch,
        capsys
    ) -> None:
    buffer = io.StringIO()
    calls = []
    def fake_sleep(x : int) -> None: calls.append(x)
    monkeypatch.setattr(time, "sleep", fake_sleep)

    Console.print("Hi", sleep=0.5, file=buffer)
    assert calls == [0.5]
    assert capsys.readouterr().out == "Hi\n"


def test_console_print_custom_file(
    ) -> None:
    buffer = io.StringIO()
    Console.print("test", file=buffer)
    assert buffer.getvalue() == "test\n"
