class Solution:
    def longestPalindrome(self, s: str) -> int:
        vals = {}
        single = 0
        ans = 0

        for c in s:
            vals[c] = vals.get(c, 0) + 1
            if vals[c] % 2 == 0:
                ans += 2

        for count in vals.values():
            if count % 2:
                ans += 1
                break
        return ans
        
