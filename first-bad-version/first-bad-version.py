# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n        
        return(self.binarySearch(n, l, r))
        
    def binarySearch(self, n, l, r):
        mid = l + (r-l)//2
        if l <= r:
            if isBadVersion(mid):
                return(self.binarySearch(n, l, mid-1))
            else:
                return(self.binarySearch(n, mid+1, r))
        return(l)