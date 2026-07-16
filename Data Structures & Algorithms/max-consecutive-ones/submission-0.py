class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1 = 0
        out = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max1 += 1
                if out < max1:
                    out = max1
            if nums[i] == 0:
                max1 = 0
        return out

            

    
        