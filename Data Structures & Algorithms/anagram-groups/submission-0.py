class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            grouped[tuple(counts)].append(s)
        return (list(grouped.values()))
            
            