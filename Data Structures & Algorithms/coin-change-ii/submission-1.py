class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = [[0] * (amount + 1) for _ in coins]
        for col in range(amount, -1, -1):
            for row in range(len(coins) - 1 , -1, -1):
                if col == amount:
                    cache[row][col] = 1
                    continue

                if col + coins[row] <= amount:
                    cache[row][col] += cache[row][col + coins[row]]
                
                if row != len(coins) - 1:
                    cache[row][col] += cache[row + 1][col]
        return cache[0][0]