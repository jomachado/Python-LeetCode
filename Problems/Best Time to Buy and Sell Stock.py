from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxPriceSell = 0

        while(right < len(prices)):
            if(prices[left] < prices[right]):
                result =  prices[right] - prices[left]
                maxPriceSell = max(result, maxPriceSell)
            else:
                left =right
            
            right += 1
        
        return maxPriceSell 


prices = [2,1,2,1,1,1,0]
obj = Solution()
print(obj.maxProfit(prices))

            


