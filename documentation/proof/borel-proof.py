import argparse

default_list = "abcdefghijklmnopqrstuvwxyz"

parser = argparse.ArgumentParser(description="Replace '*' characters in input_string with characters from the list of glyphs")

parser.add_argument('--list', '-l', type=str, default=default_list, help='list of glyphs to proof')

args = parser.parse_args()
encoded_lc = args.list

character_list = []

for char in encoded_lc:
    character_list.append(char)

print(f"making proof for {character_list}")

input_string = "* *n n*n n* o* o*n c* c*n y* y*n"

replacement_index = 0
result = []

for char in character_list:
    modified_string = input_string.replace("*", char)
    print(modified_string)


