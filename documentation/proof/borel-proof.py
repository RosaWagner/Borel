input_string = "* *n n*n n* o* o*n c* c*n y* y*n"
character_list = ["a", "á", "â", "ä", "à", "ã", "æ", "b", "c", "ç","d", "e", "é", "ê", "ë", "è", "f", "g", "ğ",
    "h", "i", "ı", "í", "î", "ï", "ì", "j", "ȷ", "k", "l", "m", "n", "ñ", "o", "ó", "ô", "ö", "ò", "õ", "œ", "p", "q", "r", "s", "ş", "ß",
    "t", "u", "ú", "û", "ü", "ù", "v", "w", "x", "y", "z"]

replacement_index = 0
result = []

for char in character_list:
    modified_string = input_string.replace("*", char)
    print(modified_string)



