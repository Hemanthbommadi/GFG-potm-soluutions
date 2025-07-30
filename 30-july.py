class Solution:
    def cntSubarrays(self, arr, k):
        cnt = 0
        currSum = 0
        mpp = {}
        for num in arr:
            currSum += num
            if currSum == k:
                cnt += 1
            comp = currSum - k
            if comp in mpp:
                cnt += mpp[comp]
            mpp[currSum] = mpp.get(currSum, 0) + 1
        return cnt
