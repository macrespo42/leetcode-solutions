def two_sum(nums: list[int], target: int):
    nums_map = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums_map.keys():
            return [i, nums_map.get(complement)]
        nums_map[n] = i
    return []


print(two_sum([2, 7, 11, 15], 9))
