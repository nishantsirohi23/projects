nums = [0,1,2,2,3,0,4,2]
val = 2

count = 0
for i in nums:
    if i==val:
        count += 1

for i in range(count):
    nums.remove(val)

print(len(nums))