import regex as re


def encode(word):
    s = ""
    cmp = 0
    for i in range(len(word)):
        if i == 0 or word[i] == word[i - 1]:
            cmp += 1
        else:
            if cmp > 1:
                s += str(cmp)
            s += word[i - 1]
            cmp = 1
    if cmp > 1:
        s += str(cmp)
    s += word[-1]
    return s


def decode(word):
    decoded_string = re.sub(r'(\d+)([\S\s])', lambda match: int(match.group(1)) * match.group(2), word)
    return decoded_string

