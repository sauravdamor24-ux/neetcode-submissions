class Solution:

    def encode(self, strs: List[str]) -> str:
        grp=[]
        for word in strs:
            length = str(len(word))
            new_word=length+"#"+word
            grp.append(new_word)
        result="".join(grp)
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        decode=[]
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            count = int(s[i:j])
            word = s[j+1:j+1+count]
            i=j+1+count
            decode.append(word)
        return decode
