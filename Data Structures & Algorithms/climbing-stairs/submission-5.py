class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        i = 2
        stairs = [0] * (n + 1)
        stairs[0] = 1
        stairs[1] = 1

        while i <= n:
            stairs[i] = stairs[i - 1] + stairs[i - 2]
            i += 1
        
        return stairs[n]
        

