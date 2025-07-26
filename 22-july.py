class Solution:
    def missingNumber(self, arr):
        v = [False] * 1000010
        for x in arr:
            if x > 0:
                v[x] = True
        for i in range(1, 100000):
            if not v[i]:
                return i
        return -1