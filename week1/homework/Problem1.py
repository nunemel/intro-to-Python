#creates constant variables for ingredients
CONST_STR_PROJECT = "cake"
CONST_INT_DIFFICULTY = 3
CONST_STR_MARGARINE = "margarine"
CONST_STR_EGGS = "eggs"
CONST_STR_APPLES = "apples"
CONST_STR_BUTTER  = "butter"
CONST_STR_FLOUR = "flour"
CONST_STR_SUGAR = "sugar"
CONST_STR_COCOA_POWDER = "cocoa powder"
CONST_STR_BAKING_POWDER = "baking powder"

flour = 175 
butter = 175 
sugar = 100 
eggs = 2 
cocoa_powder = 1 
baking_powder = 0.5

#creates dictionary for our ingredients
ingredients = {CONST_STR_FLOUR : flour, 
               CONST_STR_BUTTER : butter, 
               CONST_STR_SUGAR: sugar, 
               CONST_STR_EGGS: eggs, 
               CONST_STR_COCOA_POWDER: cocoa_powder, 
               CONST_STR_BAKING_POWDER: baking_powder}

#creates constants for print messages
CONST_STR_INGREDIENTS_CONTAIN = "Ingredients contain"
CONST_STR_INGREDIENTS_DOES_NOT_CONTAIN = "Ingredients doesn't contain"
CONST_STR_AND = "and"
CONST_STR_OR = "or"
CONST_STR_EITHER = "either"
CONST_STR_BOTH = "both"

#creates tuple for "contains" and "doesn't contain" messages
printMessage = (lambda: CONST_STR_INGREDIENTS_DOES_NOT_CONTAIN, 
       lambda: CONST_STR_INGREDIENTS_CONTAIN)
print(printMessage[CONST_STR_APPLES in ingredients](), CONST_STR_APPLES) 
print(printMessage[CONST_STR_BUTTER in ingredients](), CONST_STR_BUTTER) 
print(printMessage[(CONST_STR_EGGS in ingredients
      or CONST_STR_MARGARINE in ingredients)](), CONST_STR_EITHER, CONST_STR_EGGS, CONST_STR_OR, CONST_STR_MARGARINE)
print(printMessage[(CONST_STR_EGGS in ingredients
      and CONST_STR_MARGARINE in ingredients)](), CONST_STR_BOTH, CONST_STR_EGGS, CONST_STR_AND, CONST_STR_MARGARINE)

sep = "-"
tableSpoon = "ts"
gram = "g"
#loops through dictionary and prints the ingridients
for key, value in ingredients.items():
    if ((key == CONST_STR_COCOA_POWDER) 
        or (key == CONST_STR_BAKING_POWDER)):
        print(key.capitalize(), sep, value, tableSpoon)
    elif(key == CONST_STR_EGGS):
        print(key.capitalize(), sep, value)
    else:
        print(key.capitalize(), sep, value, gram)