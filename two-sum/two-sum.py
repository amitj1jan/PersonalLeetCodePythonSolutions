class Solution:
    '''
    written by amitjha@umich.edu
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for ind,num in enumerate(nums):
            if (target - num) in hash_map:
                return([nums.index(target-num), ind])
            else:
                hash_map[num] = 1            