import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    A = 50
    # "3A" = 130
    B = 30
    "2B" = 45
    C = 20
    D = 15

    formatted_skus = skus.upper()
    A_list = re.findall("formatted_skus", "A")
    B_list = re.findall("formatted_skus", "B")
    C_list = re.findall("formatted_skus", "C")
    D_list = re.findall("formatted_skus", "D")
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



