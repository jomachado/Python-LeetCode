from locale import currency
from turtle import position
from typing import  List
class Solution:
    def countBits(self, n: int) -> List[int]:
        cache = [0]
        nextExpo2 = 2
        currExpo2 = 1
        i =1
        while(i <= n):
            previousValues = cache[i-currExpo2]
            previousValues += 1
            cache.append(previousValues)
            i+=1
            if(i == nextExpo2):
                nextExpo2 = nextExpo2 *2
                currExpo2 = currExpo2 * 2
        return cache

obj = Solution()
print(obj.countBits(8))