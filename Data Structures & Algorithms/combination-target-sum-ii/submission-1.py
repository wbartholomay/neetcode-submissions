class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtracking(index, path):
            total = sum(path)
            if total == target:
                result.append(path[:])
                return
            if total > target or index == len(candidates):
                return
            
            path.append(candidates[index])
            backtracking(index+1, path)
            path.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1

            backtracking(index+1, path)
            
        backtracking(0, [])
        return result