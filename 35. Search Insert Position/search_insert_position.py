class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
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
        return i

sol: Solution = Solution()
numbers: list[int] = [-1,0,5,9,12]
print(sol.searchInsert(numbers, 3))
