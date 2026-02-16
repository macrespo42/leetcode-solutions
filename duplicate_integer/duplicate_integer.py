def has_duplicate(nums: list[int]) -> bool:
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False