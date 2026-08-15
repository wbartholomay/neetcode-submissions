class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            if current_sum > result:
                result = current_sum

        return result           