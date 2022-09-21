def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    mid = (l + r) // 2

    while l <= r:
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r) // 2
        
    return -1
