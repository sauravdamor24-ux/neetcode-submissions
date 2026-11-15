class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0]*26

        for char in s:
            index= ord(char)-ord('a')
            counter[index]+=1

        for char in t:
            index= ord(char)-ord('a')
            counter[index]-=1
        
        for values in counter:
            if values == 0:
                continue
            else: 
                return False
        return True