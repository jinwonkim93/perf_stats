import functools
import time
from typing import Union


def get_default_logger():
    return PerfLogger().get_logger()

def log_latency_checker(_func=None, *, logger ):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):         
            start = time.time()
            ret = func(*args, **kwargs)
            total_time = time.time() - start
            messege = f"{total_time} s"
            logger.debug(messege)
            return ret
        return wrapper
    if _func is None:
        return decorator_log
    else:
        return decorator_log(_func)
