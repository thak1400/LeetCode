class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=[1]*len(nums)
        # map={key:1 for key in range(0,len(nums))}
        for i in range(0,len(nums)):
            savedVal=answer[i]
            # answer=list(map(lambda x:x*nums[i],answer))
            answer=[nums[i]*j for j in answer]
            answer[i]=savedVal
        return answer
