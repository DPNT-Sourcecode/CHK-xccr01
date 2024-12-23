

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    A = 50
    B = 30
    C = 20
    D = 15
    for item in skus.upper():
        if item == "A":
            total += 50
        if item == "B":
            total += 30
        if item == "C":
            total += 20
        if item == "D":
            total +=15
    return total


