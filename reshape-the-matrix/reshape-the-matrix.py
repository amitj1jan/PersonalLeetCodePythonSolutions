import itertools
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        cnt = len(mat) * len(mat[0])
        if cnt != r * c:
            return(mat)
        out = [[0 for num in range(c)] for num in range(r)]
        m = len(mat)
        n = len(mat[0])
        nums = itertools.chain(*mat)
        for i in range(r):
            for j in range(c):
                out[i][j] = next(nums)
        return(out)