from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_c = Counter(ransomNote)
        magazine_c = Counter(magazine)        
        return(not ransom_c - magazine_c)