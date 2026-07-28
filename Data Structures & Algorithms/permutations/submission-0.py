class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 

        def backtracking(remaining_nums : List[int], current : List[int]):
            if len(remaining_nums) == 0:
                result.append(current)

            for  i, num in enumerate(remaining_nums):
                new_cur = current[:]
                new_cur.append(num)
                backtracking(remaining_nums[:i] + remaining_nums[i+1:], new_cur)

        backtracking(nums, [])

        return result