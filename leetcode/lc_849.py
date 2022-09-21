# https://leetcode.com/problems/maximize-distance-to-closest-person/solution/

def maxDistToClosest(seats: list[int]) -> int:
    n = len(seats)
    
    idx = 0
    max_s = 0
    while idx < n:
        if seats[idx]:
            idx += 1
            continue

        count = 0
        while idx < n and not seats[idx]:
            count += 1
            idx += 1
        
        temp_c = count // 2 + 1 if count % 2 else count // 2
        if idx >= n and count >= max_s:
            max_s = count
        elif idx - count == 0 and count >= max_s:
            max_s = count
        elif max_s <= temp_c:
            max_s = count // 2 + 1 if count % 2 else count // 2
        
        idx += 1
    
    return max_s

print(maxDistToClosest([1,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0]))