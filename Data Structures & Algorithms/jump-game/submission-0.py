class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_dest = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if cur_dest - i <= nums[i]:
                cur_dest = i
        return cur_dest == 0