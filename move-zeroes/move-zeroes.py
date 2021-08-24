class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = nums.count(0)        
        nums[:] = [num for num in nums if num !=0]
        nums+= [0] * cnt
        
        