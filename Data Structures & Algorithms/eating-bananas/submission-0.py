class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while (l <= r):
            k = (l + r) // 2
            result = 0
            for pile in piles:
                result += math.ceil(pile / k)
            if result <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
            