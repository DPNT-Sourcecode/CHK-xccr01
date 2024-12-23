import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    A_cost = 50
    # "3A" = 130
    B_cost = 30
    B_deal = 45
    C_cost = 20
    D_cost = 15

    formatted_skus = skus.upper()
    A_list = re.findall("A", formatted_skus)
    B_list = re.findall("B", formatted_skus)
    C_list = re.findall("C", formatted_skus)
    D_list = re.findall("D", formatted_skus)

    
    # calculate total cost of B including the special offers
    if len(B_list)%2 == 0:
        B_total = len(B_list)/2 * B_deal
    else:
        B_total = (len(B_list) - 1)/2 * B_deal + B_cost

    total = len(A_list)*A_cost + B_total + len(C_list)*C_cost + len(D_list)*D_cost
    return total


