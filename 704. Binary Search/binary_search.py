class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """binary search function, searches for target in a list of numbers.

        Args:
            nums (List[int]): list of sorted unique numbers to search in
            target (int): number to search for

        Returns:
            int: index of number found, -1 if not found
        """        
        i: int = 0
        j: int = len(nums) - 1
        
        first: int = nums[i]
        last: int = nums[j]

        while i <= j:
            k: int = int((i+j)/2)
            if target > nums[k]:
                i = k + 1
            elif target < nums[k]:
                j = k - 1
            else:
                return k
        return -1

sol: Solution = Solution()
numbers: list[int] = [3]
print(sol.search(numbers, 3))