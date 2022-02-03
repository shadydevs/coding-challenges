def sortedSquares(self, nums: List[int]) -> List[int]:
    newNums = []
    for n in nums:
        newNums.append(n*n)
    return sorted(newNums)
