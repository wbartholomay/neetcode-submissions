class Solution:
    def climbStairs(self, n: int) -> int:
        ways_to_climb = [0] * n 
        for i in range(n):
            ways = 0
            if i == 0:
                ways = 1
            elif i == 1:
                ways = 2
            else:
                ways = ways_to_climb[i-1] + ways_to_climb[i-2]   
            ways_to_climb[i] = ways
        print(ways_to_climb)
        return ways_to_climb[-1]