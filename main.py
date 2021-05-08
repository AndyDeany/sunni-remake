import sys
import traceback


try:
    from lib.session import Session

    session = Session()
    session.loop()
except Exception:
    with open("../crash.log", "w") as crash_log:
        crash_log.writelines(traceback.format_exception(*sys.exc_info()))
    raise
