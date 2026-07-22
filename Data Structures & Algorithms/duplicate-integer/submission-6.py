class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates_hashmap = {}
        for num in nums:
            if duplicates_hashmap.get(num) == None:
                duplicates_hashmap[num] = 1
            else:
                return True
        return False