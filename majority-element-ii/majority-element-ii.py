from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3
        lst = Counter(nums).most_common(3)[:3]
        out = []
        for key,count in lst:
            if count > majority:
                out.append(key)
            else:
                break
        return(out)
        