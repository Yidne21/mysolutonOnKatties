res = 0
for i in range(1, 5+1):
    sum = 0
    nums = input()
    nums = nums.split()
    for n in nums:
        sum += int(n)
    if res < sum:
        res = sum
        win = i
print("{} {}".format(win, res))

