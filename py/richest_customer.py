import functools
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totals = []
        for customer in accounts:
            totals.append(functools.reduce(lambda a, b: a+b, customer))
        return max(totals)
        
method_caller = Solution()
print(method_caller.maximumWealth([[1,2,3],[3,2,1]]))