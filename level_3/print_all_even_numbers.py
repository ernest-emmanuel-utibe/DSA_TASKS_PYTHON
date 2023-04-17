nums = range(1, 1000)


# create a function called is_prime that takes a single number that returns false when the number is not prime
# but returns true if the number is prime
def is_prime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
        return True

    primes = list(filter(is_prime, nums))
    print(primes)
