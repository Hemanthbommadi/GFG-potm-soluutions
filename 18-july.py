class Solution:
    def lcm(self, a, b):
        return a * b // math.gcd(a, b)

    def lcmTriplets(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        
        if n % 2 == 0:
            if n % 3 != 0:
                return n * (n - 1) * (n - 3) // math.gcd(n, n - 1) // math.gcd((n * (n - 1)) // math.gcd(n, n - 1), n - 3)
            else:
                return (n - 1) * (n - 2) * (n - 3) // math.gcd(n - 1, n - 2) // math.gcd(((n - 1)*(n - 2)) // math.gcd(n - 1, n - 2), n - 3)
        else:
            return n * (n - 1) * (n - 2) // math.gcd(n, n - 1) // math.gcd((n * (n - 1)) // math.gcd(n, n - 1), n - 2)