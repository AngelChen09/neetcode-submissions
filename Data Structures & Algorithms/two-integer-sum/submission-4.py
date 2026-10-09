class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums[i+1:]:
                idx = nums.index(remainder, i+1)
                return [i, idx]