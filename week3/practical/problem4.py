import argparse

list4 = [23, 45, 46, 78]
print("before the change", list4)
parser = argparse.ArgumentParser()
parser.add_argument("arg1", type=str)
args = parser.parse_args()
if args.arg1 in list4:
    list4 = list4.remove(args.arg1)
print("after the change", list4)
