# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if 100 < x < 0:
        raise ValueError("number not within accepted range of 0 - 100")
    if y < 0:
        raise ValueError("number not within accepted range 0 - 100")

    return x + y
    


