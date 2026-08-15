class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = [float('inf')] * len(nums)
        cache[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            cache[i] = 1 + min(cache[i:i + nums[i] + 1])
        return cache[0]