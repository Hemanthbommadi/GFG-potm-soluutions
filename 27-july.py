class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)
        m = len(mat[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_cols:
                    mat[i][j] = 0

        return mat

