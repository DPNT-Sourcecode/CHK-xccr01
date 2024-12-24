import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) is not str or skus.islower():
        return -1
    if re.search("[^A-Z]", skus) :
        return -1
    
    total = 0

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
    # total += len(re.findall("S", skus)) * 30
    # total += len(re.findall("T", skus)) * 20
    total += __calculate_bsogsof(len(re.findall("U", skus)), 4, len(re.findall("U", skus))) * 40
    total += __calculate_multi_deal(len(re.findall("V", skus)), 50, 2, 90, 3, 130)
    total += len(re.findall("W", skus)) * 20
    # total += len(re.findall("X", skus)) * 90
    # total += len(re.findall("Y", skus)) * 10
    # total += len(re.findall("Z", skus)) * 50
    total += __calculate_group_deal(skus)
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

def __calculate_group_deal(skus):
    S_cost = 20
    T_cost = 20
    X_cost = 17
    Y_cost = 20
    Z_cost = 21
    S_number = len(re.findall("[S]", skus))
    T_number = len(re.findall("[T]", skus))
    Y_number = len(re.findall("[Y]", skus))
    X_number = len(re.findall("[X]", skus))
    Z_number = len(re.findall("[Z]", skus))
    total_cost = 0

    total_number_items = len(re.findall("[STXYZ]", skus))
    if total_number_items >= 3:
        total_cost = total_number_items//3 * 45
        if total_number_items%3 == 0:
            return total_cost
        elif total_number_items%3 == 1:
            if X_number != 0:
                total_cost += 17
                return total_cost
            elif Y_number != 0 or T_number != 0 or S_number != 0:
                total_cost += 20
                return total_cost
            else:
                total_cost += 21
                return total_cost
        elif total_number_items%3 == 2:
            return 0
    else:
        return S_cost * S_number + T_cost * T_number + Y_cost * Y_number + X_cost * X_number + Z_cost * Z_number
    return total_cost

    # group_discount_items_21 = len(re.findall("Z", skus))
    # if  group_discount_items_21 != 0:
    #     group_discount_items_total - group_discount_items_21
    # elif len(re.findall("[STY]", skus)) != 0:
    # elif len(re.findall("X", skus)) != 0:

    # number_of_discounts = group_discount_items_total//3
    # if group_discount_items_total == 0:
    #     return 0
    # elif group_discount_items_total < 3:
    #     return S_cost * S_number + T_cost * T_number + Y_cost * Y_number + X_cost * X_number + Z_cost * Z_number
    # elif group_discount_items_total%3 == 0:
    #     (group_discount_items_total - group_discount_items_total%3)/3 * 45
    # elif group_discount_items_total - group_discount_items_21 > 0:
    #     return (group_discount_items_total - group_discount_items_21) + (group_discount_items_total - group_discount_items_total%3)/3 * 45
    # get rid of z first
    # get rid of s t and x
    # then get rid of y 

    # only matters if not %3 of total number of groups
    # current ammount//3 * 45 + left over items
    # new ammount = current_ammount - z_ammount
    # new_ammount == 1

    # new_ammount == 2
    # else:
    #     new_ammount -= 
    # ammount = re.findall("[STXYZ]", skus)
        
    
        
    
        
            
    
