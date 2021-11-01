class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1        
        return(self.binarySearch(nums, l, r, target))
        
    def binarySearch(self, nums, l, r, target):     
        mid = l + (r-l)//2
        if l <= r:
            if target == nums[mid]:
                return(nums.index(target))
            elif target < nums[mid]:
                return(self.binarySearch(nums, 0, mid-1, target))
            else:
                return(self.binarySearch(nums, mid+1, r, target))
        return(-1)

                