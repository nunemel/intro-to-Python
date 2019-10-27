import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help = "Please enter any text", type=str)
parser.add_argument("start_index", help = "Please enter the start index", type=int)
parser.add_argument("end_index", help = "Please enter the end index", type=int)
args = parser.parse_args()
start = args.start_index
end = args.end_index

print("""The given text: %s 
Start index: %s 
End index: %s 
Output string: %s""" % (args.str, start, end, args.str[start: end]))
