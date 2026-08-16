class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_cost = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(net_cost) < 0:
            return -1
        result = 0
        total_cost = 0
        for i, cost in enumerate(net_cost):
            total_cost += cost
            if total_cost < 0:
                result = i + 1
                total_cost = 0
            
        return result