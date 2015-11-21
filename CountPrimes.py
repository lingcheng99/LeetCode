"""
Count the number of prime numbers less than a non-negative number, n
My solution used Sieve of Eratosthenes
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        if n<=2:
            return 0
        else:
            sieve=[True]*n
            sieve[0]=False
            sieve[1]=False
            for i in range(2,int(sqrt(n))+1):
                if sieve[i]:
                    for j in range(i*i,n,i):
                        sieve[j]=False
            return sum(sieve)
