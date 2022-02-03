def searchInsert(nums: list[int], target: int) -> int:
    
    i: int = 0
    j: int = len(nums) - 1

    while i <= j:
        k: int = int((i+j)/2)
        if target > nums[k]:
            i = k + 1
        elif target < nums[k]:
            j = k - 1
        else:
            return k
    return i

def sortedSquares(nums: list[int]) -> list[int]:
#         sorted()
    neg = []
    pos = []
    for n in nums:
        if n < 0:
            neg.append(n*n)
        else:
            pos.append(n*n)

    for n in neg:
        pos.insert(searchInsert(pos, n), n)
    return pos

print(sortedSquares([-4,-1,0,3,10]))