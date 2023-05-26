def distance(first, second):
    distance = 0
    for letter, letter2 in zip(first, second):
        if letter != letter2:
            distance +=1

    return distance


