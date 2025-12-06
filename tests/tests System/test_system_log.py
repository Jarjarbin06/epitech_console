import pytest


from epitech_console.System import Log


def test_log_reading(
    ) -> None:
    log = Log("tests/", "log_test")
    assert log.read() == "   date          time      | [type_] title    | detail\n\n---START---\n0000-00-00 00:00:00.000000 | [INFO_] info     | this is an information\n0000-00-00 00:00:00.000000 | [VALID] valid    | this is a validation\n0000-00-00 00:00:00.000000 | [WARN_] warn     | this is a test3\n0000-00-00 00:00:00.000000 | [ERROR] error    | this is a test4\n>>> this is a custom comment\n----END----\n\n"