import random
import math

def miller_rabin_test(N, i=10):
    """
    Perform the Miller-Rabin primality test on the number N.
    returns true if the test is inconclusive/fails and N could be prime, and false otherwise if it is composite
    """
    if N == 2 or N == 3:
        return True
    if N == 1 or N % 2 == 0:
        return False

    #writing N as 2^k*q
    k = 0
    q = N - 1
    while q % 2 == 0:
        k += 1
        q //= 2
        
    #witness loop ( repeating i times unless broken by the return )
    for j in range(k):
        #choosing a random int between 2 and N-1-1 or N-2
        a = random.randint(2, N - 2)
        #breaks the loop if the gcd ever is not 1 (N is divisible by a or a product of it, automatically making it not prime)
        if math.gcd(a, N) != 1:
            return False

        #defines x as a to the q mod N
        x = pow(a, q, N)

        #if x is ever 1 or -1, it will skip to the next iteration of the for loop above (k+1)
        if x == 1 or x == N - 1:
            continue

        for j in range(k - 1):
            x = pow(x, 2, N)

            #searching for when x = -1modN
            if x == N - 1:
                break
        else:
            return False
    
    #only returns true if all of the iterations are also true
    return True

#example
#primality_test = 222334565193647  
#iterations = 100       

#result = miller_rabin_test(primality_test, iterations)
#print(primality_test, "is", ('probably prime' if result else 'composite'))

primes_list = []
primes_count = 0
for i in range(1000):
    result = miller_rabin_test(i, 100)
    if(result):
        primes_list.append(i)
        primes_count = primes_count + 1
print(primes_list)
print(primes_count)
