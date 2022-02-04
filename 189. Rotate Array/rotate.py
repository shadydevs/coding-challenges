def rotate(nums: list[int], k: int) -> None:
    if k == len(nums) or k == 0:
        return

    size = len(nums)
    extension = []

    for i in range(k):
        index = (size + i - k) % size
        extension.append(nums[index])

    newL = extension + nums[:-k]
    for i in range(size):
        nums[i] = newL[i]

nu = [1,2]
rotate(nu,5)
print  (nu)
