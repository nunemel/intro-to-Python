#6
products = {"candy": 10, "juice": 5, "pen": 50}

def check(product, num):
    if ((product, num) is None or not isinstance(num, int)):
        return False
    return product in products and products[product] >= num
