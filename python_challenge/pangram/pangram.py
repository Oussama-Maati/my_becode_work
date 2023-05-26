
def is_pangram(word):
    alphabet = []
    for letter in word:
        if letter not in alphabet:
            alphabet.append(letter)
    return len(alphabet)-1 >= 26