import argparse

set1 = {12, 34, 56, 78}
print(set1)
parser = argparse.ArgumentParser()
parser.add_argument("setVal", type=int)
args = parser.parse_args()
set1.add(args.setVal)
print(set1)
