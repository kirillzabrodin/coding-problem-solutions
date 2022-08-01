from typing import List

class Solution:
    def binary_search_r(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] > target: 
                right = mid - 1
            else:
                left = mid + 1
        return right
    
    def binary_search_l(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] < target: 
                left = mid + 1
            else:
                right = mid - 1
        return left
            
        
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.binary_search_l(nums, target), self.binary_search_r(nums, target)
        return (left, right) if left <= right else [-1, -1]
        
        
res = Solution()
print(res.searchRange([5,7,7,8,8,10], 8))