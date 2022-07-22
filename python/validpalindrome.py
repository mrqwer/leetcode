class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = ""
        for i in s:
            if i.isdigit() or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
                if i.isupper():
                    ns+=i.lower()
                else:
                    ns+=i
        def isPal(ns: str) -> bool:
            for i in range(len(ns)//2):
                if ns[i] != ns[len(ns)-1-i]: return False
            return False
        isPal(ns)
        
