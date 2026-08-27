class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ''
        best = float('inf')
        need = {}
        window = {}
        have = 0
        for i in t:
            need[i] = need.get(i,0) + 1
        req = len(need)

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in need and need[s[r]] == window[s[r]]:
                have += 1
            
            while have == req:
                if r-l+1 < best:
                    best = r-l+1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l+=1
        return res