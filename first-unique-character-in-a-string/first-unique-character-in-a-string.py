class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        res = []
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        for item in dic:
            if dic[item] == 1:
                res.append(s.index(item))
        if len(res) >0:
            return(min(res))
        else:
            return(-1)        
        
        