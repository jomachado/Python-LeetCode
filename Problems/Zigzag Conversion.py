import re
from turtle import pos, position


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""        
        for level in range(0, numRows, 1):            
            position = level
            positionMidle = level
            while(position < len(s)):                
                result += s[position]
                if(level > 0 and level < numRows-1):
                    positionMidle =  position +  ((numRows-1)*2) - (2*level)
                    if(positionMidle < len(s)):
                        result += s[positionMidle]
                position += (numRows- 1)* 2
                
        return result

s =  "A"
rows = 1
obj = Solution()
print(obj.convert(s, rows))
            

#PINALSIGYAHRPI        
