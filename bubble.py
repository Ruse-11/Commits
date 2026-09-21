nums = [10, 3, -19, 34, 12, -86, 122, 0, 1, 12]
n = len(nums)
for i in range(n-1):
    mini = i
    for j in range(i+1, n):
        if nums[mini] > nums[j]:
            mini = j
    nums[i], nums[mini] = nums[mini], nums[i]

print(*nums)