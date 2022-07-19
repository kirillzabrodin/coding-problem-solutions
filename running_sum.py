from typing import List

def running_sum(nums: List[int]) -> List[int]:
        sums = [nums[0]]
        for i in nums[1:len(nums)]:
            sums.append(sums[-1] + i)
        return sums
    
print(running_sum([1,2,3,4]))