import argparse

set2 = {12, 34, 56, 78}
print(set2)
parser = argparse.ArgumentParser()
parser.add_argument("setVal", type=int)
args = parser.parse_args()
set2.add(args.setVal)