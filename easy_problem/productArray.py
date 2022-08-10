import math
nums = input()
nums = nums.split()
nums = list(map(int, nums))
res = [0] * len(nums)
ind = 0
hashmap = {}
for i in nums:
    nums.pop(ind)
    res[ind] = math.prod(nums)
    nums.insert(ind, i)
    ind += 1
print(res)
