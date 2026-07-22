class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countPerLetter ={}
        for letter in s:
            if letter in countPerLetter:
                countPerLetter[letter] += 1
            else:
                countPerLetter[letter] = 1
        for letter in t:
            if letter in countPerLetter:
                if countPerLetter[letter] <=0:
                    return False
                else:
                    countPerLetter[letter] -= 1
            else:
                return False
        for letter in countPerLetter:
            if countPerLetter[letter] !=0:
                return False
        return True
