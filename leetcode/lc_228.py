# https://leetcode.com/problems/summary-ranges/

# https://leetcode.com/problems/summary-ranges/discuss/1806040/Python-easy-O(n)-solution-or-explained

def summaryRanges(nums: list[int]) -> list[str]:
    res = []
    
    p_idx = 0
    n_idx = 1
    while n_idx < len(nums) + 1:
        t_idx = p_idx
        while n_idx < len(nums) and nums[t_idx] + 1 == nums[n_idx]:
            t_idx = n_idx
            n_idx += 1
        if p_idx == t_idx:
            res.append(f"{nums[p_idx]}")
        else:
            res.append(f"{nums[p_idx]}->{nums[t_idx]}")
        p_idx = n_idx
        n_idx += 1
    
    return res