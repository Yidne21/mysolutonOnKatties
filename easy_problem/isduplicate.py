num = input()
nums = []
nums = num.split()
isduplicate = False
hashset = set()
for n in nums:
    if n in hashset:
        isduplicate = True
        break
    hashset.add(n)
print(isduplicate)