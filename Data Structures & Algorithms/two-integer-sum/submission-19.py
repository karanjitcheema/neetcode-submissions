class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for num in nums:
            if sum.get(num) is None:
                sum[num] =1
            else:
                sum[num] =2 
        for key in nums:
            if key == (target-key) and sum.get(key)==2:
                break
            elif key!=(target-key) and sum.get(target-key) is not None:
                break
        print(key)
        if key == target-key:
            return [nums.index(key), max(i for i, x in enumerate(nums) if x == key)]
        else:
            return [nums.index(key), nums.index(target-key)]