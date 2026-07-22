class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for str in strs:
            count = [0]*26
            for letter in str:
                count[ord(letter)-ord('a')] +=1
            letterCount = tuple(count)
            if letterCount in grouped.keys():
                grouped[letterCount].append(str)
            else:
                grouped[letterCount] = [str]
        finalList = []
        for group in grouped:
            finalList.append(grouped[group])
        return finalList