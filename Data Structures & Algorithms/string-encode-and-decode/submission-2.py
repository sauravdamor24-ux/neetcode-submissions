class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for word in strs:
            length = str(len(word))
            new_word = length+"#"+word
            encode.append(new_word)
        result = "".join(encode)
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        decode=[]
        while i<len(s):
            while s[j]!="#":
                j+=1
            count=int(s[i:j])
            word = str(s[j+1:j+1+count])
            decode.append(word)
            i= j+1+count
            j = i
        return decode

