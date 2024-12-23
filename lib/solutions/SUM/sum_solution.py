# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or x > 100:
        raise ValueError("number not within accepted range of 0 - 100")
    if y < 0 or y > 100:
        raise ValueError("number not within accepted range 0 - 100")

    return x + y
    



