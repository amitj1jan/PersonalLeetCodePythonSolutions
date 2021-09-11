class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        cnt = len(mat) * len(mat[0])
        if cnt != r * c:
            return(mat)
        out = [[0 for num in range(c)] for num in range(r)]
        m = len(mat)
        n = len(mat[0])
        mat_flat = [0 for num in range(m) for num in range(n)]
        indx=0
        for i in range(m):
            for j in range(n):
                mat_flat[indx] = mat[i][j]
                indx += 1
        indx = 0
        for i in range(r):
            for j in range(c):
                print(i, j, out[i])
                out[i][j] = mat_flat[indx]
                indx += 1
        return(out)