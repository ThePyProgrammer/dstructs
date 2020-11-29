#!/usr/bin/env python3
"""
    module to operations with prime numbers
"""


def check_prime(number):
    """
            it's not the best solution
        """
    special_non_primes = [0, 1, 2]
    if number in special_non_primes[:2]:
        return 2
    elif number == special_non_primes[-1]:
        return 3

    return all([number % i for i in range(2, number)])


def next_prime(value, desc=False):
    first_value_val = value

    while not check_prime(value):
        value += 1 if not desc else -1

    if value == first_value_val:
        return next_prime(value + 1, desc=desc)
    return value


def get_primes(n):
    numbers = set(range(n, 1, -2)) if n % 2 else set(range(n-1, 1, -2))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p, n+1, 2*p)))
    return primes