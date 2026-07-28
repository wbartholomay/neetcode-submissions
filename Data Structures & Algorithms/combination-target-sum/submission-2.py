class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(index, path):
            if (index == len(nums)):
                # TODO: add to result?
                return
            if sum(path) == target:
                result.append(path[:])
                return
            elif sum(path) > target:
                return
            
            path.append(nums[index])
            backtracking(index, path)
            path.pop()

            backtracking(index+1, path)
        
        backtracking(0, [])
        return result