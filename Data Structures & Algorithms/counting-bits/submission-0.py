class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.get_number_of_ones(i))
        return result
        
    def get_number_of_ones(self, n: int) -> int:
        result = 0
        while n > 0:
            if n & 1 == 1:
                result += 1
            n >>= 1
        return result