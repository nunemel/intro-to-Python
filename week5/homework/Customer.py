#6cont.
import Productcheck as pc

def buy(product, num, price):
    if ((product, num, price) is None or not isinstance(num, int) or not isinstance(price, int)):
        raise Exception("Please add correct parameters.")
    if pc.check(product, num):
        print("You bought %s and spent %d" % (product, num * price))
    else:
        "Sorry! We are out of this product."

def main():
    buy("juice", 4, 20)

if __name__ == "__main__":
    main()




