import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help = "Add any text", type=str)
parser.add_argument("first_word", help = "Add first word", type=str)
parser.add_argument("second_word", help = "Add second word", type=str)

args = parser.parse_args()
text = args.text
first_word = args.first_word
second_word = args.second_word

if len(text) >= len(first_word):
    output_string = args.text.replace(first_word, second_word)
    print("""The given text: %s 
The first word: %s
The second word: %s
The output string: %s""" % (text, first_word, second_word, output_string))
else:
    print("The length of the text argument must be greater or equals to the length of the first_word argument")
