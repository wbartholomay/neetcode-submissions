class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = [0] * len(cost)
        for i in range(len(cost) - 1, -1, -1):
            if i == len(cost) - 1 or i == len(cost) - 2:
                min_costs[i] = cost[i]
            else:
                min_costs[i] = cost[i] + min(min_costs[i+1], min_costs[i+2])
        return min(min_costs[0], min_costs[1])
