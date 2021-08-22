class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return(nums.index(target))
        else:
            left = 0
            right = len(nums) -1
            while right >= left:
                mid = left + (right-left)//2
                if target > nums[right]:
                    return(right+1)
                elif target < nums[left]:
                    return(left)
                elif ((right == left +1) and (target > nums[left]) and (target < nums[right])):
                    return(right)
                elif target > nums[mid]:
                    left = mid +1
                else:
                    right = mid
            
                    
        