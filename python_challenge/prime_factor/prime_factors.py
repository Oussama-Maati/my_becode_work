import math


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False

    return True


def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1

    return factors

