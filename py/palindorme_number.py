import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        for i in range(math.floor(int(len(number))/2)):
            if number[i] != number[len(number) - i - 1]:
                return False
        return True
        
res = Solution()
print(res.isPalindrome(1221))