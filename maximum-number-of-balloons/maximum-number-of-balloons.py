from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        minCnt = 10**4
        src_str = 'balloon'
        for char in set(src_str):
            if char in text:                
                cnt = text.count(char)//src_str.count(char)
                if cnt < minCnt:
                    minCnt = cnt
            else:
                minCnt = 0
                break
        return(minCnt)