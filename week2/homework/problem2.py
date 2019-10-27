import argparse, math

parser = argparse.ArgumentParser()
parser.add_argument("text", help = "Add text wich has 7 or more odd number characters", type=str)
args = parser.parse_args()
text = args.text
if (len(text) >= 7 and (len(text) & 1) == 1):
    middle_index = int(len(text)/2)
    start_index = middle_index - 1 
    end_index = middle_index + 2
    middleThreeChars = text[start_index:end_index]
    new_string = "".join((text[:start_index], middleThreeChars.upper(), text[end_index:]))
    print("""The old string: %s
Middle 3 characters: %s
The new string: %s""" % (text, middleThreeChars, new_string))
else:
    print("The text doesn't contain 7 or more and odd number characters")        
