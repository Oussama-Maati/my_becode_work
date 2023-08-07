import string

alphabet = list(string.ascii_lowercase)

print(alphabet)


def encode(word):
    encoded_word = ""
    five = 0
    for letter in word.lower().replace(' ', '').replace(",", "").replace(".", ""):

        if letter.isalpha():
            index = alphabet.index(letter)
            encoded_word += list(reversed(alphabet))[index]
        else:
            encoded_word += str(letter)
        five += 1
        if five == 5:
            encoded_word += " "
            five = 0
    return encoded_word.rstrip()


def decode(word):
    decoded_word = ""
    for letter in word.lower():
        if letter.isalpha():
            decoded_word += alphabet[25 - alphabet.index(letter)]
        else:
            decoded_word += letter
    return decoded_word.replace(" ", "")

