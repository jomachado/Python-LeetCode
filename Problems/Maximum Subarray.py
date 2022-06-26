from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currencySum = 0
        result = nums[0]

        for i in range(0, len(nums), 1):
            currencySum += nums[i]
            result = max(result, currencySum)   
        
            if(currencySum < 0):
                currencySum = 0
        return result


obj = Solution()
nums = [10,-7,1,11]
print(obj.maxSubArray(nums))
