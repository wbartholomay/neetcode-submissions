class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtracking(index, cur):
            if index == len(nums):
                result.append(cur[:])
                return

            cur.append(nums[index])
            backtracking(index+1, cur)
            cur.pop()

            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtracking(index+1, cur)

        backtracking(0,[])
        return result