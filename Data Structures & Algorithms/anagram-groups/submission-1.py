class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            s[key].append(word)
        return list(s.values())