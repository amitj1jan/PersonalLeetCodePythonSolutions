class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        hash_map = {}
        for i,num in enumerate(nums):
            if (num not in hash_map) and (i%10 == num):
                hash_map[num] = i
        print(hash_map)
        if hash_map.values():            
            return(min(hash_map.values()))
        return(-1)