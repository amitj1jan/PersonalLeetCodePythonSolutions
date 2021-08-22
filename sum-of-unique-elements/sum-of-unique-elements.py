class Solution:
    '''
    created by amitj1jan
    '''    
    def sumOfUnique(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] = 0
        return(sum([key for key,val in hash_map.items() if val ==1 ]))
        