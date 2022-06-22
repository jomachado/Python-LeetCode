from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCombinations = dict()
        for i in range(len(nums)):
            sub = target - nums[i]
            if(sub in numsCombinations):
                return [numsCombinations[sub], i]
            else:
                numsCombinations[nums[i]] = i

