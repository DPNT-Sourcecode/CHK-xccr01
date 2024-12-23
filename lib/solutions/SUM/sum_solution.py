# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if x < 0 or x > 100:
        raise ValueError("number x not within accepted range of 0 - 100")
    if y < 0 or y > 100:
        raise ValueError("number y not within accepted range 0 - 100")
    if type(x) is not int:
        raise TypeError("x must be an integer")
    if type(y) is not int:
        raise TypeError("x must be an integer")
    return x + y
    
