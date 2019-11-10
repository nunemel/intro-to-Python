import argparse

parser = argparse.ArgumentParser()
s3 = {12, 13, 45, 68, 45, 766}
parser.add_argument("setV", type=int)
args = parser.parse_args()

print(args.setV > min(s3) and args.setV < max(s3))