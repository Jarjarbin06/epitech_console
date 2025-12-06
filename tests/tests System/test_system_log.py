import pytest


from epitech_console.System import Log
from epitech_console import init, quit


init()



def test_log_reading(
    ) -> None:
    log = Log("tests", "log_test")
    log.comment("this is a custom comment")
    log.close()
    log.show()
    assert log.read() == "   date          time      | [type_] title    | detail\n\n---START---\n>>> this is a custom comment\n----END----\n"
    log.close(True)


quit(True)
