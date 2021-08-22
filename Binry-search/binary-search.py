class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        return(self.binarySearch(nums, 0, r, target))
        
    def binarySearch(self, arr, l, r, K):
        if r >=l:
            mid = l + (r-l)//2
            
            if K == arr[mid]:
                return(arr.index(K))
            elif K < arr[mid]:
                return(self.binarySearch(arr, l, mid-1, K))
            else:
                return(self.binarySearch(arr, mid+1, r, K))
        return(-1) 