from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        c = Counter(s)
        if c["A"] >= 2: return False
        count = 0
        for i in s:
            if i == "L":
                count+=1
                if count == 3: return False
            else: count = 0
        return True
