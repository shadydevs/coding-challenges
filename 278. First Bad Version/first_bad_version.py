# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """finds first n where isBadVersion returns true for

        Args:
            n (int): number of versions

        Returns:
            int: first n
        """        
        i: int = 1
        j: int = n
        
        first: int = isBadVersion(i)
        last: int = isBadVersion(j)
            
        if not isBadVersion(n-1):
            return n
        
        while i <= j:
            k: int = int((i+j)/2)
            if not isBadVersion(k):
                i = k + 1
            else:
                j = k - 1
        return i