class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        stringList = []
        i=0
        while i <len(s) -1:
            j=i
            while s[j] !='#':
                j +=1
            length = int(s[i:j])
            stringList.append( s[(j+1): (j+ 1+  length) ] )
            i= j+1 + length
        return stringList