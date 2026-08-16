class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        result = 0
        total_cost = 0
        for i in range(len(gas)):
            total_cost += (gas[i] - cost[i])

            if total_cost < 0:
                result = i + 1
                total_cost = 0
            
        return result