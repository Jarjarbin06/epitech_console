import pytest

from epitech_console.Animation.animation import Animation


# ============================================================
# Animation Class
# ============================================================

def test_animation_initialization_with_list(
    ) -> None:
    frames = ["A", "B", "C"]
    anim = Animation(frames)
    assert anim.animation == frames
    assert anim.step == 0
    assert anim.render() == "A"


def test_animation_initialization_with_string(
    ) -> None:
    anim = Animation("X\\Y\\Z")
    assert anim.animation == ["X", "Y", "Z"]
    assert anim.render() == "X"


def test_animation_update_basic(
    ) -> None:
    anim = Animation(["A", "B", "C"])
    assert anim.render() == "A"
    anim.update()
    assert anim.render() == "B"
    anim.update()
    assert anim.render() == "C"


def test_animation_update_auto_reset_enabled(
    ) -> None:
    anim = Animation(["A", "B"])
    anim.update()  # index 1
    anim.update()  # auto-reset to 0
    assert anim.render() == "A"


def test_animation_update_auto_reset_disabled(
    ) -> None:
    anim = Animation(["A", "B"])
    anim.update(auto_reset=False)
    anim.update(auto_reset=False)
    # Stays on last frame
    assert anim.render() == "B"


def test_animation_render_delete_flag(
    ) -> None:
    anim = Animation(["A"])
    output = anim.render(delete=True)
    # Output MUST include delete sequence and frame
    assert isinstance(output, str)
    assert "A" in output


def test_animation_length_magic_method(
    ) -> None:
    anim = Animation(["A", "B", "C"])
    assert len(anim) == 3
