class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = sorted([abs(num) for num in nums])
        return([num**2 for num in nums])