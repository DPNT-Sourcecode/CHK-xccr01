import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) is not str or skus.islower():
        return -1
    if re.search("[^ABCDE]", skus) :
        return -1
    total = 0
    A_cost = 50
    A_deal_3 = 130
    A_deal_5 = 200
    B_cost = 30
    B_deal = 45
    C_cost = 20
    D_cost = 15
    E_cost = 40

    skus = skus.upper()
    A_list = re.findall("A", skus)
    B_list = re.findall("B", skus)
    C_list = re.findall("C", skus)
    D_list = re.findall("D", skus)
    E_list = re.findall("E", skus)

    # calculate total cost of A including the special offers
    A_items = len(A_list)
    if A_items == 1:
        A_total = A_cost
    elif A_items == 2:
        A_total = A_cost * 2
    elif A_items%5 == 0:
        A_total = A_items/5 * A_deal_5
    elif A_items%3 == 0:
        A_total = A_items/3 * A_deal_3
    elif A_items == 4:
        A_total = ((A_items - A_items%3)/3 * A_deal_3) +(A_items%3 * A_cost)
    else:
        A_total = ((A_items - A_items%5)/5 * A_deal_5) +(A_items%5 * A_cost)

    B_items = len(B_list)
    E_items = len(E_list)
    #calculate effect of E on B
    if E_items >= 2:
        E_items//2
        B_items = B_items - E_items//2
    # calculate total cost of B including the special offers
    if B_items%2 == 0:
        B_total = B_items/2 * B_deal
    else:
        B_total = (B_items - 1)/2 * B_deal + B_cost

    
    


    total = A_total + B_total + len(C_list)*C_cost + len(D_list)*D_cost + E_items*E_cost
    return total
