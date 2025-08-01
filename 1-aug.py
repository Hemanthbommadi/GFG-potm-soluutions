class Solution:
    def countBalanced(self, arr):
        def isVowel(ch):
            return ch in 'aeiou'
        
        from collections import defaultdict

        preSum = 0
        ans = 0
        freq = defaultdict(int)
        freq[0] = 1  # for the empty prefix

        for s in arr:
            for ch in s:
                if isVowel(ch):
                    preSum += 1
                else:
                    preSum -= 1
            ans += freq[preSum]
            freq[preSum] += 1
        
        return ans
