# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

def longestSubarray(self, nums: list[int]) -> int:
    segs = [] # array of segments with start and end of the 1's sequence
              # saves [l, r)
    
    if 0 not in nums:
        return len(nums) - 1
    
    idx = 0
    lhs = -1
    rhs = -1
    while idx < len(nums):
        if not nums[idx]:
            idx += 1
            continue
        lhs = idx
        while idx < len(nums) and nums[idx]:
            idx += 1
        rhs = idx
        segs.append((lhs, rhs))
    
    if not segs:
        return 0
    
    max_one = segs[0][1] - segs[0][0]
    lhs, rhs = segs[0]
    for l, r in segs[1:]:
        cur_max = r - l
        if l - rhs == 1:
            max_one = max(max_one, r - lhs - 1)
        else:
            max_one = max(cur_max, max_one)
        lhs, rhs = l, r
    
    return max_one
