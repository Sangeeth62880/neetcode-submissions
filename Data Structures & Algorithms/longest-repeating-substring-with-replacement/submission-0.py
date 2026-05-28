class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        max_count = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if freq[s[r]] > max_count:
                max_count = freq[s[r]]
            if (r - l + 1 - max_count > k):
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res