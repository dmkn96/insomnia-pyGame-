from script.general import *


def firstRun(self):
    def decorator(func):
        def wrapper(*args, **kwargs):
            readSettings(self)
            return func(*args, **kwargs)

        return wrapper

    return decorator
