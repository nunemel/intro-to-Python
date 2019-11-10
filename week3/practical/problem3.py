import sys, argparse

list2 = [12, 34, 56, 56]
parser = argparse.ArgumentParser()
parser.add_argument("countVal", help = "the value to be counted", type=int)
args = parser.parse_args()
print("Number of %ss = %s" % (args.countVal, list2.count(args.countVal)))