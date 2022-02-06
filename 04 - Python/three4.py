"""
*is_prime(n)
    ? takes an integer argument n and returns True if it is a prime number. It returns False if it is not.
	? A prime number is any number that is only divisible by the numbers 1 and itself(EG: 7 and 13 are prime numbers).
    ? 1 and 0 is not a prime number.    
    ! Means n will not be divisible by any number before that(which will not include 0 and 1)

*factors(n)
	? takes an integer argument n and returns a list of all of its factors,
	? that is, numbers which exactly divide n and leave no remainder (this includes 1 and n itself).
    ! Means all the number with 0 reminder in division in range n

*prime_factors(n)
	? takes an integer argument n and returns a list of all of its prime factors, that is , the factors which are prime numbers.
	? This function should make use of the is_prime() and factors() functions specified above.
    ! Means we can return factors which are only prime numbers
"""


def isPrime(n):
    is_prime = True

    if n < 2:
        is_prime = False

    for i in range(n-1, 1, -1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


def factors(n):
    factors_list = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list


def primeFactors(n):
    factors_list = factors(n)
    prime_factors = []

    for i in factors_list:
        if isPrime(i):
            prime_factors.append(i)

    return prime_factors


factors_list = factors(42)
prime_factors = primeFactors(42)
print(factors_list)
print(prime_factors)
factors_list = factors(100)
prime_factors = primeFactors(100)
print(factors_list)
print(prime_factors)