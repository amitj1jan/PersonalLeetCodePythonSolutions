from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums)//2
        key,count = Counter(nums).most_common(1)[0]
        if count >= majority:
            return(key)
        
        