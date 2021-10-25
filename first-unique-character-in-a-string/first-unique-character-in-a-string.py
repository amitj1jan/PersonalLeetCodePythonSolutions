class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for indx,char in enumerate(s):
            if char not in hash_map:
                hash_map[char] = indx 
            else:
                hash_map[char] = 99999
        if min(hash_map.values()) == 99999:
            return(-1)
        else:
            return(min(hash_map.values()))        
        