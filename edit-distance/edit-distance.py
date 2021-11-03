class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dis = [[0] * (n+1) for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dis[i][j] =j
                elif j == 0:
                    dis[i][j] =i
                elif word1[i-1] == word2[j-1]:
                    dis[i][j] = dis[i-1][j-1]
                else:
                    dis[i][j]=   (1 + min(dis[i][j-1], dis[i-1][j], dis[i-1][j-1]))
                                  
        return(dis[m][n])