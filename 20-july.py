class Solution:
    def countValid(self, n, arr):
        all_digits = set(str(i) for i in range(10))
        blocked_digits = all_digits - set(str(d) for d in arr)

        blocked_digits = list(blocked_digits)
        blocked_count = len(blocked_digits)
        
        if blocked_count == 0:
            return 9 * (10 ** (n - 1))

        def count_invalid():
            if blocked_count == 0:
                return 0
            count = 0
            for i in range(10 ** (n - 1), 10 ** n):
                if all(ch in blocked_digits for ch in str(i)):
                    count += 1
            return count

        total = 9 * (10 ** (n - 1))

        if '0' in blocked_digits:
            start_digits = [d for d in blocked_digits if d != '0']
        else:
            start_digits = blocked_digits

        if len(start_digits) == 0:
            invalid = 0
        else:
            invalid = len(start_digits) * (len(blocked_digits) ** (n - 1))

        return total - invalid