class Solution:
    '''
    written by amitjha@umich.edu
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = -inf
        for num in nums:
            current_sum = max(num, current_sum+num)
            best_sum = max(current_sum, best_sum)
        return(best_sum)