import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) is not str or skus.islower():
        return -1
    if re.search("[^A-Z]", skus) :
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

    
    

    total += __calculate_multi_deal(len(re.findall("A", skus)), 50, 3, 130, 5, 200)
    total += __calculate_simple_deal(__calculate_bsogsof(len(re.findall("E", skus)), 2, len(re.findall("B", skus))), 30, 2, 45)
    total += len(re.findall("C", skus)) * 20
    total += len(re.findall("D", skus)) * 15
    total += len(re.findall("E", skus)) * 40
    total += __calculate_simple_deal(len(re.findall("F", skus)), 10, 3, 20)
    total += len(re.findall("G", skus)) * 20
    total += __calculate_multi_deal(len(re.findall("H", skus)), 10, 5, 45, 10, 80)
    total += len(re.findall("I", skus)) * 35
    total += len(re.findall("J", skus)) * 60
    total += __calculate_simple_deal(len(re.findall("K", skus)),80, 2, 150)
    total += len(re.findall("L", skus)) * 90
    total += __calculate_simple_deal(__calculate_bsogsof(len(re.findall("N", skus)), 3, len(re.findall("M", skus))), 15, 0, 0)
    total += len(re.findall("N", skus)) * 40
    total += len(re.findall("O", skus)) * 10
    total += __calculate_simple_deal(len(re.findall("P", skus)), 50, 5, 200)
    total += __calculate_simple_deal(__calculate_bsogsof(len(re.findall("R", skus)), 3, len(re.findall("Q", skus))), 30, 3, 80)
    total += len(re.findall("R", skus)) * 50
    total += len(re.findall("S", skus)) * 30
    total += len(re.findall("T", skus)) * 20
    total += __calculate_bsogsof(len(re.findall("U", skus)), 4, len(re.findall("U", skus))) * 40
    total += __calculate_multi_deal(len(re.findall("V", skus)), 50, 2, 90, 3, 130)
    total += len(re.findall("W", skus)) * 20
    total += len(re.findall("X", skus)) * 90
    total += len(re.findall("Y", skus)) * 10
    total += len(re.findall("Z", skus)) * 50
    return total

def __calculate_multi_deal(items, reg_cost, deal1_ammount, deal1_cost, deal2_ammount, deal2_cost):
    if items < deal1_ammount:
        total = items * reg_cost

    elif items >= deal2_ammount:
        if items%deal2_ammount == 0:
            total = items/deal2_ammount * deal2_cost

        elif (items%deal2_ammount) < deal1_ammount:
            total = ((items - items%deal2_ammount)/deal2_ammount * deal2_cost) +(items%deal2_ammount * reg_cost)

        elif items%deal2_ammount == deal1_ammount:
            total = ((items - deal1_ammount)/deal2_ammount * deal2_cost) + deal1_cost

        elif items%deal2_ammount > deal1_ammount:
            total = ((items - items%deal2_ammount)/deal2_ammount * deal2_cost) + deal1_cost + (items%deal2_ammount - deal1_ammount) * reg_cost
    elif items%deal1_ammount == 0:
        total = deal1_cost
    elif items > deal1_ammount and items < deal2_ammount:
        total = ((items - items%deal1_ammount)/deal1_ammount * deal1_cost) + items%deal1_ammount * reg_cost
    else:
        total = 0
    
    return total

def __calculate_bsogsof(bought_items, bought_items_deal, free_items):
    if free_items == 0:
        return 0
    if bought_items >= bought_items_deal:
        free_items = free_items - bought_items//bought_items_deal
    return free_items

def __calculate_simple_deal(items, cost, deal, deal_cost):
    total = 0
    if items < deal or deal == 0:
        total = items * cost
    elif items >= deal:
        if items%deal == 0:
            total = items/deal * deal_cost
        else:
            total = ((items - items%deal)/deal *deal_cost) + (items%deal * cost)
    else:
        return total

    return total




