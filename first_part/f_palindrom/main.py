sentence = input().lower()
compound_sentence = ''
for letter in sentence:
    if (48 <= ord(letter) <= 57) or (97 <= ord(letter) <= 122):
        compound_sentence += letter


is_palindrom = compound_sentence == compound_sentence[::-1]
print(is_palindrom)

