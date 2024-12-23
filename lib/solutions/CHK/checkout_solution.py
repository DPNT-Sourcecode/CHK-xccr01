import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) is not str or skus.islower():
        return -1
    if re.search("[^ABCDEF]", skus) :
        return -1
    total = 0
    C_cost = 20
    D_cost = 15
    E_cost = 40

    skus = skus.upper()
    A_items = len(re.findall("A", skus))
    B_items = len(re.findall("B", skus))
    C_items = len(re.findall("C", skus))
    D_items = len(re.findall("D", skus))
    E_items = len(re.findall("E", skus))
    F_items = len(re.findall("F", skus))

    # calculate total cost of A including the special offers
    # if items == 1:
    #     A_total = A_cost
    # elif items == 2:
    #     A_total = A_cost * 2
    # elif items%5 == 0:
    #     A_total = items/5 * A_deal_5
    # elif items%3 == 0:
    #     A_total = items/3 * A_deal_3
    # elif items == 4:
    #     A_total = ((items - items%3)/3 * A_deal_3) +(items%3 * A_cost)
    # else:
    #     A_total = ((items - items%5)/5 * A_deal_5) +(items%5 * A_cost)

    # #calculate effect of E on B
    # if E_items >= 2:
    #     E_items//2
    #     B_items = B_items - E_items//2
    # # calculate total cost of B including the special offers
    # if B_items%2 == 0:
    #     B_total = B_items/2 * B_deal
    # else:
    #     B_total = (B_items - 1)/2 * B_deal + B_cost

    
    


    total = __calculate_multi_deal(A_items) + __calculate_free_item(B_items, E_items) + __calculate_F(F_items, 10, )
    return total

def __calculate_multi_deal(items):
    # calculate total cost of A including the special offers
    if items == 0:
        return 0
    A_cost = 50
    A_deal_3 = 130
    A_deal_5 = 200
    if items == 1:
        A_total = A_cost
    elif items == 2:
        A_total = A_cost * 2
    elif items == 3:
        A_total = A_deal_3
    elif items == 4:
        A_total = A_deal_3 + A_cost
    elif items >=5 :
        if items%5 == 0 :
            A_total = items/5 * A_deal_5
        elif items%5 < 3:
            A_total = ((items - items%5)/5 * A_deal_5) +(items%5 * A_cost)
        elif items%5 == 3:
            A_total = ((items - 3)/5 * A_deal_5) + A_deal_3
        elif items%5 == 4:
            A_total = ((items - 4)/5 * A_deal_5) + A_deal_3 + A_cost
    else:
            A_total = 0
    
    return A_total

def __calculate_free_item(B_items, E_items):
    if B_items == 0:
        return 0
    B_cost = 30
    B_deal = 45

    #calculate effect of E on B
    if E_items >= 2:
        E_items//2
        B_items = B_items - E_items//2
    # calculate total cost of B including the special offers
    if B_items%2 == 0:
        B_total = B_items/2 * B_deal
    else:
        B_total = (B_items - 1)/2 * B_deal + B_cost
    
    return B_total

def __calculate_F(items, cost, deal):
    total = 0
    cost = 10
    F_deal = 20
    if items == 1 or items == 2:
        total = items * cost
    if items >= 3:
        if items%3 == 0:
            F_total = items/3 * deal
        else:
            F_total = ((items - items%3)/3 *deal) + (items%3 * cost)
    else:
        return F_total

    return F_total

