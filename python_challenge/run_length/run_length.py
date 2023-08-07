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


# def encode(string):
#     num_letter = 1
#     final = ""
#     for index, letter in enumerate(string):
#         if index+1 < len(string) and letter == string[index+1] :
#             num_letter += 1
#         else:
#             final += str(num_letter)+str(letter)
#             num_letter = 1
#
#     final = final.replace("1", "")
#     return final

def decode(word):
    decoded_string = re.sub(r'(\d+)([\S\s])', lambda match: int(match.group(1)) * match.group(2), word)
    return decoded_string
