class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr3 = [None] * (m+n)
        i, j, k =0,0,0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr3[k] = nums1[i]
                k += 1
                i += 1
            elif nums1[i] > nums2[j]:
                arr3[k] = nums2[j]
                k += 1
                j += 1

        while i < m:
            arr3[k] = nums1[i]
            k += 1
            i += 1

        while j < n:
            arr3[k] = nums2[j]
            k += 1
            j += 1
        nums1[:] = arr3[:]
        return
                    
        