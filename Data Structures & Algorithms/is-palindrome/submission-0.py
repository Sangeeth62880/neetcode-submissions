class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        clean = "".join(c.lower() for c in s if c.isalnum())
        right = len(clean) - 1
        while left < right:
            if clean[left] != clean[right]:
                return False
            left += 1
            right -= 1
        return True
