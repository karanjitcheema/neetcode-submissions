class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] +=1
            else:
                map[num] = 1
        found = False
        i=0
        for i in range(len(nums)):
            if nums[i] == target /2:
                if map[nums[i]] >1:
                    found = True
                    break
            else:
                if ((target - nums[i]) in map) :
                    found = True
                    break
        for j in range(len(nums)):
            if (nums[i] == target/2):
                if (nums[j] == target-nums[i]) & (j>i):
                    break
            elif nums[j] == target-nums[i]:
                break
        return [i, j]
