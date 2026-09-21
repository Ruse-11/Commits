nums = [10, 3, -19, 34, 12, -86, 122, 0, 1, 12]
n = len(nums)
for i in range(1, n):
    key = nums[i]
    for j in range(i):
        if key <= nums[j]:
            nums.insert(j, key)
            nums.pop(i + 1)
            break

for i in range(1, n):
    key = nums[i]
    while 
print(*nums)


"""

5 6 2

"""