import pytest

from epitech_console.Animation.animation import Animation
from epitech_console.Animation.progressbar import ProgressBar
from epitech_console.Animation.spinner import Spinner


# ============================================================
# ProgressBar Class
# ============================================================

def test_progressbar_initialization(
    ) -> None:
    pb = ProgressBar(10)
    assert pb.length == 10
    assert pb.percent == 0
    assert pb.style.on == "#"
    assert pb.style.off == "-"
    assert isinstance(pb.animation, Animation) or pb.animation is None


def test_progressbar_update_basic(
    ) -> None:
    pb = ProgressBar(10)
    pb.update(50)
    assert pb.percent == 50


def test_progressbar_update_spinner_flag(
    ) -> None:
    sp = Spinner.plus()
    pb = ProgressBar(10, spinner=sp)

    first = pb.spinner.render()
    pb.update(20, update_spinner=True)
    second = str(pb.spinner.render())

    assert first != second


def test_progressbar_update_no_spinner_update(
    ) -> None:
    sp = Spinner.plus()
    pb = ProgressBar(10, spinner=sp)

    first = pb.spinner.render()
    pb.update(20, update_spinner=False)
    second = str(pb.spinner.render())

    assert first == second


def test_progressbar_render_basic(
    ) -> None:
    pb = ProgressBar(10)
    pb.update(40)
    result = str(pb.render())
    assert isinstance(result, str)
    assert "[" in result and "]" in result


def test_progressbar_render_hide_spinner_at_end(
    ) -> None:
    sp = Spinner.stick()
    pb = ProgressBar(10, spinner=sp)

    pb.update(100)
    result = str(pb.render(hide_spinner_at_end=True))

    assert isinstance(result, str)
    assert sp.render() not in result  # spinner hidden


def test_progressbar_render_delete_flag(
    ) -> None:
    pb = ProgressBar(10)
    result = str(pb.render(delete=True))
    assert isinstance(result, str)


def test_progressbar_percent_style_bar(
    ) -> None:
    pb = ProgressBar(10, percent_style="bar")
    pb.update(60)
    text = str(pb.render())
    # Expect filling using style.on
    assert "#" in text


def test_progressbar_percent_style_number(
    ) -> None:
    pb = ProgressBar(10, percent_style="num")
    pb.update(60)
    text = str(pb.render())
    # Expect percentage
    assert text.split()[-1] == "60%"


def test_progressbar_percent_style_mix(
    ) -> None:
    pb = ProgressBar(length=10, percent_style="mix")
    pb.update(60)
    text = str(pb.render())
    # Mix style includes both bar and percent digits
    assert "#" in text
    assert "%" in text
