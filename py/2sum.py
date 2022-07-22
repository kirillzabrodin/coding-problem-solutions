from typing import List


def TwoSum(nums: List[int], target: int) -> List[int]:
    adict = {}
    
    for i in range(len(nums)):
        if ((target - nums[i]) in adict):
            return [nums[i], adict[target-nums[i]]] 
        else:
            adict.update(nums[i], i)


TwoSum([1,2,3,4], 7)