"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes < 1:
        raise ValueError 

    start = 2 
    while len(list) < number_of_primes:
        if(isPrime(start)):
            list.append(start)
        start += 1

    return list

def isPrime(p):
    if p == 1 or p == 0:
        return False
    for i in range(2, p):
        if p%i == 0:
            return False
    return True


print(primes(20))