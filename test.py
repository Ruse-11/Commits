def dup(nums):
    n = len(nums)
    for i in range(n):      # n
        for j in range(i-1):    #n-1
            if nums[j] == nums[i]:
                return True
    return False

'''
    O(n*n) --> O(n^2)
'''
'''
key, value = reg, name
'''
d = {}

d[337] = "Ram"
d[338] = "jai"

print(d)
