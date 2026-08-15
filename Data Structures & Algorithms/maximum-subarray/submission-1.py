class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        def dfs(i, current_sum):
            nonlocal result
            if current_sum > result:
                result = current_sum
            
            if i == len(nums):
                return

            if current_sum < 0:
                current_sum = 0
            dfs(i+1, current_sum + nums[i])
        
        dfs(1, nums[0])


        return result           