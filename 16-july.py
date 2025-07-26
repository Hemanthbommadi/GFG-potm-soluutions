
class Solution:
    def countNumbers(self, n):
        limit = int(math.sqrt(n)) + 1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, limit, i):
                    is_prime[j] = False

        primes = [i for i, val in enumerate(is_prime) if val]
        count = 0

        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                prod = primes[i] ** 2 * primes[j] ** 2
                if prod <= n:
                    count += 1
                else:
                    break

        return count