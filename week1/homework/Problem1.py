CONST_STR_MARGARINE = "margarine"
CONST_STR_EGGS = "eggs"
CONST_STR_APPLES = "apples"
CONST_STR_BUTTER  = "butter"
CONST_STR_FLOUR = "flour"
CONST_STR_SUGAR = "sugar"
CONST_STR_COCOA_POWDER = "cocoa powder"
CONST_STR_BAKING_POWDER = "baking powder"
difficulty = 3
project = "cake"

flour = 175 
butter = 175 
sugar = 100 
eggs = 2 
cocoa_powder = 1 
baking_powder = 0.5


ingredients = {CONST_STR_FLOUR : flour, 
               CONST_STR_BUTTER : butter, 
               CONST_STR_SUGAR: sugar, 
               CONST_STR_EGGS: eggs, 
               CONST_STR_COCOA_POWDER: cocoa_powder, 
               CONST_STR_BAKING_POWDER: baking_powder}

print(CONST_STR_APPLES in ingredients) 
print(CONST_STR_BUTTER in ingredients)
print((CONST_STR_EGGS in ingredients) or (CONST_STR_MARGARINE in ingredients))
print((CONST_STR_EGGS in ingredients) and (CONST_STR_MARGARINE in ingredients))

sep = "-"
tableSpoon = "ts"
gram = "g"
for x,y in ingredients.items():
    if ((x == CONST_STR_COCOA_POWDER) or (x == CONST_STR_BAKING_POWDER)):
        print(x, sep, y, tableSpoon)
    elif(x == CONST_STR_EGGS):
        print(x, sep, y)
    else:
        print(x, sep, y, gram)