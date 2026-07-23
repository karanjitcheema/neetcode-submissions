class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        i=0
        j=len(nums)-1
        while i<len(nums):
            if i==0:
                prefix[i]=1
            else:
                prefix[i] = prefix[i-1]*nums[i-1]
            i+=1
        while j>=0:
            if j==len(nums)-1:
                suffix[j]=1
            else:
                suffix[j] = suffix[j+1]*nums[j+1]
            j-=1
        output = [1] * len(nums)
        i=0
        for i in range(len(nums)):
            output[i] = prefix[i]* suffix[i]
            print(output[i])
        return output
        