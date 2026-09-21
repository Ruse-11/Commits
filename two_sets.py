n = int(input())
set1 = []
set2 = []
total = (n*(n+1)) // 2
curr = 0
for num in range(n,0,-1):
    if curr+num <= total-num:
        set1.append(num)
        curr += num
        total -= num
    else:
        set2.append(num)
if curr == total:
    print("YES")
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)
else:
    print("NO")
