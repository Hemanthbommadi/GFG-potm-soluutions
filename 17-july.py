class Solution:
    def maxKPower(self, n, k):
        def prime_factors(k):
            factors = {}
            i = 2
            while i * i <= k:
                while k % i == 0:
                    factors[i] = factors.get(i, 0) + 1
                    k //= i
                i += 1
            if k > 1:
                factors[k] = factors.get(k, 0) + 1
            return factors

        def legendre(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count

        factors = prime_factors(k)
        min_power = float('inf')
        for prime, exponent in factors.items():
            power_in_n_fact = legendre(n, prime)
            min_power = min(min_power, power_in_n_fact // exponent)
        return min_power