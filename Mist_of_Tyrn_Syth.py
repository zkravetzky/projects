"""
This is a program that replicates the puzzle in the World Of Warcraft dungeon Mists Of Tirna Sithe
This puzzle gives 4 images and the objective is to find the odd symbol out.
This means that the other three symbols will have something in common that the 4th one does not.
The descriptions are:
 -flower or leaf
 -filled or not filled
 -circle border or no circle border

"""
import random
class Symbol:
    #creating a class for each of the symbols
    def __init__(self, name, is_leaf, has_circle, is_filled):
        self.name = name
        self.is_leaf = is_leaf
        self.has_circle = has_circle
        self.is_filled = is_filled
    
# function to check through all 4 symbols passed in as a list.
# The difference can be with or without that descriptor
# so we need to check if only one has it or if the other three has it

def get_odd_symbol(symbol_list):
    is_leaf = 0
    has_circle = 0
    is_filled = 0
    for symbol in symbol_list:
        if symbol.is_leaf == True:
            is_leaf += 1
        if symbol.has_circle == True:
            has_circle += 1
        if symbol.is_filled:
            is_filled += 1
    if is_leaf == 3:
        return [symbol.name for symbol in symbol_list if symbol.is_leaf == False]
    elif is_leaf == 1:
        return [symbol.name for symbol in symbol_list if symbol.is_leaf]
    elif has_circle == 3:
        return [symbol.name for symbol in symbol_list if symbol.has_circle == False]
    elif has_circle == 1:
        return [symbol.name for symbol in symbol_list if symbol.has_circle]
    elif is_filled == 3:
        return [symbol.name for symbol in symbol_list if symbol.is_filled == False]
    elif is_filled == 1:
        return [symbol.name for symbol in symbol_list if symbol.is_filled]
    else:
        get_odd_symbol(get_random_symbols(all_symbols))

def get_random_symbols(all_symbols):
    list = []
    for i in range(4):
        rand = random.randint(1,8-i)
        print(len(all_symbols))
        print(rand)
        list.append(all_symbols.pop(rand-1))
    for names in list:
        print(names.name)
    return list


symbol1 = Symbol('Leaf_Filled_Circle',True, True, True)
symbol2 = Symbol('Leaf_Filled_NoCircle',True, True, False)
symbol3 = Symbol('Leaf_NotFilled_Circle',True, False, True)
symbol4 = Symbol('Leaf_NotFilled_NoCircle',True, False, False)
symbol5 = Symbol('Flower_Filled_Circle', False, True, True)
symbol6 = Symbol('Flower_Filled_NoCircle', False, True, False)
symbol7 = Symbol('Flower_NotFilled_Circle', False, False, True)
symbol8 = Symbol('Flower_NotFilled_NoCircle', False, False, False)

all_symbols = [symbol1, symbol2, symbol3, symbol4, symbol5, symbol6, symbol7, symbol8]


#for symbol in get_random_symbols(all_symbols):
#    print(symbol.name)

print(get_odd_symbol(get_random_symbols(all_symbols)))