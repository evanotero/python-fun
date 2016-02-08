#####################################################
# Author: Evan Otero                                #
# Date: November 24, 2015                           #
# This script generates a list of divisors for n    #
# To run, use the function: divisorGen(<number>)    #
# To print results, use: print divisorGen(<number>) #
#####################################################

from math import sqrt

##### Find all prime factors of n #####
def factorize(n):
   if n < -1: return [(-1, 1)] + factorize(-n)
   elif n == -1: return [(-1, 1)]
   elif n == 0: return [(0, 1)]
   elif n == 1: return [(1, 1)]
   else:
      def potential_primes():
         base_primes = (2, 3, 5)
         for base_prime in base_primes:
            yield base_prime
         base_primes = (7, 11, 13, 17, 19, 23, 29, 31)
         prime_group = 0
         while True:
            for base_prime in base_primes:
               yield prime_group + base_prime
            prime_group += 30
      factors = []
      sqrtn = sqrt(n)
      for divisor in potential_primes():
         if divisor > sqrtn:
            break
         power = 0
         while (n % divisor) == 0:
            n //= divisor
            power += 1
         if power > 0:
            factors.append((divisor, power))
            sqrtn = sqrt(n)
      if n > 1:
         factors.append((n, 1))
      return factors

##### Find all divisors using prime factors #####
def divisors_from_factors(factors):
   def unsorted_divisors_from_factors(factors):
      if not factors: return [1]
      else:
         base, max_power = factors[0]
         if base == -1: return unsorted_divisors_from_factors(factors[1:])
         elif base == 0: return []
         elif base == 1: return unsorted_divisors_from_factors(factors[1:])
         else:
            divisors = unsorted_divisors_from_factors(factors[1:])
            all_divisors = []
            for power in xrange(0, max_power+1):
               all_divisors += map(lambda x: x * base ** power, divisors)
            return all_divisors
   all_divisors = unsorted_divisors_from_factors(factors)
   all_divisors.sort()
   return all_divisors

##### Main Function #####
def divisorGen(n):
   d = divisors_from_factors(factorize(n))
   return d

##### Find integers 0<n<1000 with largest number of divisors #####
def part_b():
   maxNumbers = []
   maxDivisor = 0
   for num in range(1,1000):
      d = divisorGen(num)
      if len(d)>maxDivisor:
         maxDivisor = len(d)
   for num in range(1,1000):
      d = divisorGen(num)
      if len(d) == maxDivisor:
         maxNumbers += [num]
   print maxNumbers

##### Find integers 0<n<1000 with odd number of divisors #####
def part_c():
   oddDivisors = []
   for num in range(1,1000):
      d = divisorGen(num)
      if len(d)%2!=0:
         oddDivisors += [num]
   print oddDivisors
