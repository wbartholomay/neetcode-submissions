class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(index) -> int:
            if index >= len(nums):
                return 0
            if cache[index] == -1:
                cache[index] = max(dfs(index + 1), nums[index] + dfs(index + 2))
            return cache[index]

        res = dfs(0)
        return res