class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_chars ={}
        for letter in s:
            if count_chars.get(letter) == None:
                count_chars[letter] = 1
            else:
                count_chars[letter] +=1
        for letter in t:
            if count_chars.get(letter) == None:
                return False
            else:
                count_chars[letter] -=1

        for remaining_letters in count_chars.keys():
            if count_chars.get(remaining_letters) !=0:
                return False
        return True
