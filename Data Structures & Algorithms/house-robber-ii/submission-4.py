class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache_1 = [-1] * (len(nums) - 1)
        cache_2 = [-1] * (len(nums) - 1)

        for i in range(len(nums) - 2, -1, -1):
            cache_1[i] = max(nums[i] + self.get_cache_val(i+2, cache_1), self.get_cache_val(i+1, cache_1))
            cache_2[i] = max(nums[i + 1] + self.get_cache_val(i+2, cache_2), self.get_cache_val(i+1, cache_2))
        
        return max(cache_1[0], cache_2[0])

    def get_cache_val(self, index: int, cache: List[int]) -> int:
        if index >= len(cache) or index < 0:
            return 0
        return cache[index]