class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_num = nums[mid]
            if mid_num == target:
                return mid
            if nums[l] <= mid_num:
                if nums[l] <= target < mid_num:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if mid_num < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1