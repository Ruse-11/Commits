import math

from collections import deque
class Solution:
    def minStep(self, num1, num2):
        def sieve():
            prime = [True] * 10000
            prime[0] = prime[1] = False

            for i in range(2, int(math.sqrt(10000)) + 1):
                if prime[i]:
                    for j in range(i * i, 10000, i):
                        prime[j] = False
            return prime

        is_prime = sieve()

        seen = {num1}
        q = deque([(num1, 0)])

        while q:
            num, step = q.popleft()

            if num == num2:
                return step

            s = list(str(num))

            for i in range(4):
                og = s[i]
                for digit in "0123456789":
                    if digit == og:
                        continue
                    s[i] = digit
                    nextt = int("".join(s))


                    if nextt >= 1000 and is_prime[nextt] and nextt not in seen:
                        seen.add(nextt)
                        q.append((nextt, step + 1))

                s[i] = og

        return -1

s = Solution()
print(s.minStep(1033, 8179))