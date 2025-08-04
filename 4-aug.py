class Solution:
    def maxRectSum(self, mat):
        n = len(mat)
        m = len(mat[0])
        ans = float('-inf')
        
        for j in range(m):
            arr = [0] * n
            for k in range(j, m):
                for i in range(n):
                    arr[i] += mat[i][k]
                
                curr_sum = 0
                for i in range(n):
                    curr_sum += arr[i]
                    ans = max(curr_sum, ans)
                    curr_sum = max(curr_sum, 0)
        
        return ans
