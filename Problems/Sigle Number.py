
from typing import List
class Solution: 
    def singleNumber(self, nums: List[int]) -> int:
            number = 0
            for item in nums:
                number = number ^ item
            return number

obj = Solution()
print(obj.singleNumber([1,3]))