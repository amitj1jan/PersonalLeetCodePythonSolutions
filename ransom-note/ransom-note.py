from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_c = Counter(ransomNote)
        magazine_c = Counter(magazine)
        magazine_c.subtract(ransom_c)
        if magazine_c.most_common()[-1][1] <0:
            return(False)
        else:
            return(True)