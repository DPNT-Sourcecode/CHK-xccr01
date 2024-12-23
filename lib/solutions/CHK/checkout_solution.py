import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    A_cost = 50
    A_deal = 130
    B_cost = 30
    B_deal = 45
    C_cost = 20
    D_cost = 15

    formatted_skus = skus.upper()
    A_list = re.findall("A", formatted_skus)
    B_list = re.findall("B", formatted_skus)
    C_list = re.findall("C", formatted_skus)
    D_list = re.findall("D", formatted_skus)

    # calculate total cost of A including the special offers
    A_items = len(A_list)
    if A_items == 1:
        A_total = A_cost
    if A_items == 2:
        A_total = A_cost * 2
    elif A_items%3 == 0:
        A_total = A_items/3 * A_deal
    else:
        A_total = (A_items - A_items%3)/3 * A_deal + A_cost * A_items%3


    # calculate total cost of B including the special offers
    B_items = len(B_list)
    if B_items%2 == 0:
        B_total = B_items/2 * B_deal
    else:
        B_total = (B_items - 1)/2 * B_deal + B_cost

    total = A_total + B_total + len(C_list)*C_cost + len(D_list)*D_cost
    return total





