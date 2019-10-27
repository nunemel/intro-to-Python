import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help = "displays any string", type=str)
args = parser.parse_args()
lowerStr = args.str.lower()
upperStr = args.str.upper()
print("The given string: %s" % args.str)
print("All lowercase: %s" % lowerStr)
print("All uppercase: %s" % upperStr)