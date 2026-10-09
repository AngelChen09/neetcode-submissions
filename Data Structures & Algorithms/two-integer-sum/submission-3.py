class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Does it have to be 2 pointer? It'll be O(n^2) runtime instead of the O(n)
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums[i+1:]:
                idx = nums.index(remainder, i+1)
                return [i, idx]