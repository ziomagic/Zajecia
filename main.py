

# Public: Find a prime factors list of number
#
# number - Target integer
#
# Example:
#       get_prime_factors_list(777)
#       # => [3, 7, 37]
#
# Returns a list of prime factors
def get_prime_factors_list(number):
    factors = list()
    d = 2
    while number > 1:
        while number % d == 0:
            factors.append(d)
            number /= d

        d += 1

    return factors


def print_max_prime_factor(number):
    print max(get_prime_factors_list(number))

print_max_prime_factor(600851475143)