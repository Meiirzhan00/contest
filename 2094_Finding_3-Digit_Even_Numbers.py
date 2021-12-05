from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        N = len(digits)
        setD = set()
        for i in range(N):
            if digits[i] != 0:
                for j in range(N):
                    if i != j:
                        for k in range(N):
                            if i!=k and j!=k and digits[k]%2==0:
                                setD.add(digits[i]*100 + digits[j]*10 + digits[k])

        return sorted(list(setD))


p = Solution()
r = p.findEvenNumbers([0, 1, 0, 0])
print(r)



....................................

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for x, y, z in permutations(digits, 3): 
            if x != 0 and z & 1 == 0: 
                ans.add(100*x + 10*y + z) 
        return sorted(ans)
