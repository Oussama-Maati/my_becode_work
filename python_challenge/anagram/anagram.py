def detect_anagrams(word, w_list):
    detected = []
    for word_in in w_list:
        if sorted(word_in) == sorted(word):
            detected.append(word_in)

    return detected
