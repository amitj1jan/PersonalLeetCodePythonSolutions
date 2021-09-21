class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        out = self.binarySearch(nums, l, r, target)                    
        return(out)

    def binarySearch(self, nums, l, r, target):
        if r >=l:
            mid = l + (r-l)//2
            if target == nums[mid]:
                    return(mid)
            elif target < nums[mid]:
                return(self.binarySearch(nums, l, mid-1, target))
            else:
                return(self.binarySearch(nums, mid+1, r, target))           
        else:
            return(-1)

            
    
        