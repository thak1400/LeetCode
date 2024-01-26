class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        answer=[1]*len(nums)
        for i in range(1,len(nums)):
            left[i]=nums[i-1]*left[i-1]
        # print(left)
        for i in range(len(nums)-1,0,-1):
            right[i-1]=nums[i]*right[i]
        # print(right)    
        for i in range(0,len(nums)):
            answer[i]=left[i]*right[i]
        return answer