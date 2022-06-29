from typing import List
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorThenSize = math.floor(len(nums)/2)
        values = dict()

        for item in nums:
            if(not item in values):
                values[item] = 0

            values[item] += 1

            if  values[item] > majorThenSize:
                return  item
            

nums = [3,2,3]
obj = Solution()

print(obj.majorityElement(nums))



        