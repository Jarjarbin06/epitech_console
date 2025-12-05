import pytest
import time


from epitech_console.System.time import Time


def test_time_wait(
    ) -> None:
        elapsed = Time.wait(0.05)

        assert 0.05 < elapsed < 0.06
