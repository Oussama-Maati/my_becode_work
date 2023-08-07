def abbreviate(sentence):
    s = ""
    for word in sentence.replace("-", " ").split():
        s += word[0].upper()
        for i, letter in enumerate(word):
            if i + 1 < len(word) and word[i + 1].isupper() and word[i].islower():
                s += word[i + 1]

    return s
