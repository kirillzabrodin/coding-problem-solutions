from typing import List, Set


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles: Set = set()
        for n in arr:
            if n in doubles:
               return True
            else: 
                doubles.add(2 * n)
                if n % 2 == 0:
                    doubles.add(n / 2)
        return False