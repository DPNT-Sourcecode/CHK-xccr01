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
    A_items = len(re.findall("A", skus))
    B_items = len(re.findall("B", skus))
    C_items = len(re.findall("C", skus))
    D_items = len(re.findall("D", skus))
    E_items = len(re.findall("E", skus))

    # calculate total cost of A including the special offers
    # if A_items == 1:
    #     A_total = A_cost
    # elif A_items == 2:
    #     A_total = A_cost * 2
    # elif A_items%5 == 0:
    #     A_total = A_items/5 * A_deal_5
    # elif A_items%3 == 0:
    #     A_total = A_items/3 * A_deal_3
    # elif A_items == 4:
    #     A_total = ((A_items - A_items%3)/3 * A_deal_3) +(A_items%3 * A_cost)
    # else:
    #     A_total = ((A_items - A_items%5)/5 * A_deal_5) +(A_items%5 * A_cost)

    # #calculate effect of E on B
    # if E_items >= 2:
    #     E_items//2
    #     B_items = B_items - E_items//2
    # # calculate total cost of B including the special offers
    # if B_items%2 == 0:
    #     B_total = B_items/2 * B_deal
    # else:
    #     B_total = (B_items - 1)/2 * B_deal + B_cost

    
    


    total = calculate_A(A_items) + calculate_B(B_items, E_items) + C_items*C_cost + D_items*D_cost + E_items*E_cost
    return total

def calculate_A(A_items):
    # calculate total cost of A including the special offers
    if A_items == 0:
        return 0
    A_cost = 50
    A_deal_3 = 130
    A_deal_5 = 200
    if A_items == 1:
        A_total = A_cost
    elif A_items == 2:
        A_total = A_cost * 2
    elif A_items == 3:
        A_total = A_deal_3
    elif A_items == 4:
        A_total = A_deal_3 + A_cost
    elif A_items >=5 :
        if A_items%5 == 0 :
            A_total = A_items/5 * A_deal_5
        elif A_items%5 < 3:
            A_total = ((A_items - A_items%5)/5 * A_deal_5) +(A_items%5 * A_cost)
        elif A_items%5 == 3:
            A_total = ((A_items - 3)/5 * A_deal_5) + A_deal_3
        elif A_items%5 == 4:
            A_total = ((A_items - 4)/5 * A_deal_5) + A_deal_3 + A_cost
    else:
            A_total = 0
    
    return A_total

def calculate_B(B_items, E_items):
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



