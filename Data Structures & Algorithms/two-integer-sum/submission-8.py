class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reverse = dict()
        for i in range(len(nums)):
            reverse[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in reverse.keys() and i != reverse[diff]:
                return [i, reverse[diff]]