from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        position = 0
        commontPrefix = ""
        for i in strs[0]:
            for y in range(0, len(strs), 1):
                if(position >= len(strs[y]) or strs[y][position] != i ):
                    return commontPrefix                
            
            commontPrefix += i
            position+=1

        return commontPrefix



obj = Solution()        
strs = ["ab","a"]    
print(obj.longestCommonPrefix(strs))
        
        

