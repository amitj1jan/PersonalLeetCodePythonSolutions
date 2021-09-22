class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1= {}
        hash2 = {}
        
        for num in nums2:
            if num in hash2:
                hash2[num] += 1
            else:
                hash2[num] = 1
        res = []
        for num in nums1:
            if num in hash2.keys() and hash2[num] >=1:
                res.append(num)
                hash2[num] -= 1
        return(res)
            