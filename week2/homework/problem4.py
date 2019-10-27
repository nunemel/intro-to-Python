import argparse

parser = argparse.ArgumentParser()
parser.add_argument("text", help = "Enter any text", type=str)
args = parser.parse_args()
old_text = args.text
text_ignore_case = args.text.casefold()
find_text = "USA".casefold()
replace_text = "Armenia"

new_string = text_ignore_case.replace(find_text, replace_text)

print("""The given string: %s
The USA/usa count is: %d 
The new string: %s""" %(old_text, text_ignore_case.count(find_text), new_string))
