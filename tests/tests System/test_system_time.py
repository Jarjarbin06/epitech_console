import pytest
import time


from epitech_console.System.time import Time


def test_time_wait(
        monkeypatch
    ) -> None:
    called = []
    def fake_sleep(v : int) -> None: called.append(v)
    monkeypatch.setattr(time, "sleep", fake_sleep)

    Time.wait(1.25)
    assert called == [1.25]


def test_time_pause(
        monkeypatch,
        capsys
    ) -> None:
    # Simulate pressing Enter
    monkeypatch.setattr("builtins.input", lambda *args: "")

    Time.pause("Press...")
    out = capsys.readouterr().out

    assert "Press..." in out


def test_time_pause_default_message(
        monkeypatch,
        capsys
    ) -> None:
    monkeypatch.setattr("builtins.input", lambda *args: "")
    Time.pause()

    out = capsys.readouterr().out
    assert "Press enter to continue..." in out
