import math
n=input()
x, y = map(int, n.split())
q=int(math.floor(x/y))
nums = input()
nums = nums.split()
for i in range (y - 1, len(nums), y):
    print(nums[i], end=" ")