#Modules
#7
def calculate_cube(x):
    if isinstance(x, int):
        return x**3

def calculate_square(x):
    if isinstance(x, int):
        return x**2

import pretty_print as pp
def main():
    pp.simple_print(calculate_square(2))
    pp.pro_print(calculate_cube(4))

if __name__ == '__main__':
    main()