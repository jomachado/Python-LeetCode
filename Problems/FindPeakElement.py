from traceback import print_tb
from typing import List

class Solution:
    def findPeak(self, nums: List[int], start, end) -> int:

        sizeArray = int(start+end)
        middleArray = int(sizeArray/2)

        if nums[middleArray] < nums[middleArray-1]:         
            return self.findPeak(nums,start, middleArray)  
        else:
            if  middleArray+1 < len(nums) and nums[middleArray] < nums[middleArray+1]:
                return self.findPeak(nums,middleArray,end)  
            else:
                return middleArray


    def findPeakElement(self, nums: List[int]) -> int:
        return self.findPeak(nums, 0, len(nums))
     


input_list = [130,141,220,316,337,4445,1222444,0]
obj = Solution()
peak = obj.findPeakElement(input_list) 

print("Pico encontrado na posição: " + str(peak) + " com valor: "+ str(input_list[peak]))