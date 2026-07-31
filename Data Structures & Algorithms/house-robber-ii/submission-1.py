class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return nums[0]
         
        nums_arrays = (nums[0:len(nums) - 1], nums[1:len(nums)])
        caches = ([-1] * (len(nums)-1), [-1] * (len(nums)-1))
        def dfs(index, array_num):
            array = nums_arrays[array_num]
            cache = caches[array_num]
            if index >= len(array):
                return 0
            if cache[index] == -1:
                cache[index] = max(dfs(index+1, array_num), array[index] + dfs(index+2, array_num))
            return cache[index]
        return max(dfs(0, 0), dfs(0, 1))