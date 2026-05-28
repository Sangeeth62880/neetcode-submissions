class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import lru_cache
        n = len(text1)
        m = len(text2)
        @lru_cache(None)
        def lcs(n,m):
            if n == 0 or m == 0:
                return 0
            if text1[n-1] == text2[m-1]:
                return lcs(n-1,m-1) + 1
            else:
                return max(lcs(n-1,m),lcs(n,m-1))
        return lcs(n,m)

