class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        need = {}
        window = {}
        have = 0
        res = ""
        min_len = float('inf')  
        for r in t:
            need[r] = need.get(r,0) + 1
        req = len(need)
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1
            while have == req:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                window[s[l]] -=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -=1
                l+=1
        return res