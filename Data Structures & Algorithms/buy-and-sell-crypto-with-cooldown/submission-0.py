class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        has_coin_cache = [-1] * len(prices)
        not_has_coin_cache = [-1] * len(prices)
        def helper(i, has_coin):
            if i >= len(prices):
                return 0
            
            if not has_coin:
                if not_has_coin_cache[i] == -1:
                    not_has_coin_cache[i] = max(helper(i+1, True) - prices[i], helper(i+1, False))
                return not_has_coin_cache[i]
            else:
                if has_coin_cache[i] == -1:
                    has_coin_cache[i] = max(helper(i+2, False) + prices[i], helper(i+1, True))
                return has_coin_cache[i]
        return helper(0, False)