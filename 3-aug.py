class Solution:
    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])
        arr = [[0] * m for _ in range(n)]

        for op in opr:
            v, r1, c1, r2, c2 = op

            arr[r1][c1] += v

            if c2 + 1 < m:
                arr[r1][c2 + 1] -= v
                if r2 + 1 < n:
                    arr[r2 + 1][c2 + 1] += v

            if r2 + 1 < n:
                arr[r2 + 1][c1] -= v

        for i in range(n):
            for j in range(1, m):
                arr[i][j] += arr[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                arr[i][j] += arr[i - 1][j]

        for i in range(n):
            for j in range(m):
                arr[i][j] += mat[i][j]

        return arr
