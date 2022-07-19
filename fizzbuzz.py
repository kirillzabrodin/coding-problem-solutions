from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        for i in range(1, n+1):
            string_result = ""
            if i % 3 == 0:
                string_result += "Fizz"
            if i % 5 == 0:
                string_result += "Buzz"
            output.append(string_result if string_result != "" else str(i))
        return output
        
        
result = Solution()
print(result.fizzBuzz(3))