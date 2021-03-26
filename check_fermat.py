# ultimo teorema de Fermat
# b**n + c**n = a**n
# if 'n' is a prime number and 'a' is a positive integer less then 'n'
# then a**n modulo n = a modulo 'n'.

def is_prime_number():
    num = int(input('Enter a number:'))
    if num > 1:
        for i in range(num):
            if (num % i) == 0:
                print(num,'is not a prime number')
                print(i,'times', num//i, 'is',num)
                break
            else:
                print(num,'it is a prime number')
    else:
        print(num,'is not a prime numer')

# n = 2
# a = 1
# 1**2 % 2 == 1
# n < 3, a E [1,2]
# 1**3 mod3 = 1
#
# 1**2 % 2 == 1
# 1**3 % 3 == 1
# 2**3 % 3 == 2
# 1**5 & 5 == 1
# 2**5 & 5 == 2
#
# given a number 'n', we want to test if it is prime
#
# 1. Pick a roundom number 'a' E [1, n-1]
# 2. Check if a**n % n == a
# 3. if yes return true
# 4. if no, return false
# import random
# random.seed()
# print(random.randint(1,10))
# print(is_fermat_prime(2,10))
# find_fermat_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
is_prime_number()

