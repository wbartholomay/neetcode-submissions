class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, cur_sum):
            if i == len(nums):
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            cache_key = (i, cur_sum)
            if cache.get(cache_key) is None:
                cache[cache_key] = dfs(i+1, cur_sum - nums[i]) + dfs(i+1, cur_sum + nums[i])
            return cache[cache_key]
        return dfs(0, 0)