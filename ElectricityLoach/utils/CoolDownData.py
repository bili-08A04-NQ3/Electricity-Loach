import time

CoolDown: dict = {}


def reset(thing: str):
    try:
        diff = - CoolDown[thing] + time.time()
        return diff > 10
    except:
        CoolDown[thing] = time.time()
        return True
