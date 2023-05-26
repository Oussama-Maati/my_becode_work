import re
from collections import defaultdict


def word_count(sentence):
    words = re.findall(r'\b[\w\'\-]+\b', sentence, re.UNICODE)
    words = [re.split(r'[_🤚👋🖐️✋🖖👌🤙🤜🤛👐🙌👏]', word) for word in words]
    words = [item for sublist in words for item in sublist]
    word_count = defaultdict(int)
    for word in words:
        word_count[word.lower()] += 1
    return dict(word_count)

