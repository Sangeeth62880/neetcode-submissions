class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        def solve(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                nonlocal res
                if r-l+1 > len(res):
                    max_len = r-l+1
                    res = s[l:r+1]
                l -=1
                r+=1
        
        for i in range(len(s)):
            solve(i,i)
            solve(i,i+1)
        return res