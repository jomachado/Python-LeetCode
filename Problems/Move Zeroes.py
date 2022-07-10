from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0

        while(right < len(nums)):
            if(nums[right] != 0):
                nums[left], nums[right] = nums[right], nums[left]                
                left+=1
            right+=1
        
        print(nums)

        return None

nums = [1,0,0,3,12]
obj = Solution()
obj.moveZeroes(nums)


        

