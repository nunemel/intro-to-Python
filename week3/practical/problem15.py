import sys, argparse

dict1 = {1 : 'hj', 2: '4fg', 3 : 'ffgh'}
print("Before change dict1 = ", dict1)
parser = argparse.ArgumentParser()
parser.add_argument("strKey", type=str)
parser.add_argument("strValue", type=str)
args = parser.parse_args()
dict1[args.strKey] = args.strValue