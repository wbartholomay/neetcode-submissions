class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            cache[i] = max(nums[i] + self.get_cache_val(i + 2, cache), self.get_cache_val(i + 1, cache))
        return cache[0]
    

    def get_cache_val(self, index: int, cache: List[int]) -> int:
        if index >= len(cache):
            return 0
        return cache[index]