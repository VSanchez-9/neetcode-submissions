class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsS = {}
        countsT = {}
        for ch in s: 
            if ch in countsS:
                countsS[ch] += 1
            else:
                countsS[ch] = 1
        
        for ch in t:
            if ch in countsT:
                countsT[ch] += 1
            else:
                countsT[ch] = 1
        if countsS == countsT:
            return True
        else: 
            return False


