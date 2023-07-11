def square_of_sum(num):
    sum = 0
    for i in range(num+1):
        sum += i

    return sum**2

def sum_of_squares(num):
    sum = 0
    for i in range(num + 1):
        sum += i**2

    return sum

def difference(num):
    sum = 0
    for i in range(num + 1):
        sum += i

    sum = sum ** 2

    sum2 = 0
    for i in range(num + 1):
        sum2 += i**2

    return sum - sum2
