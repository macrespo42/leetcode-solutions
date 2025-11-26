def two_sum(nums: list[int], target: int):
    map = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in map.keys():
            return [i, map.get(complement)]
        map[n] = i
    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
