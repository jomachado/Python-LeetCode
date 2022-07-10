class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: 
            return 0
                     
        l = 0 
        r = len(needle)-1
        while(r <= len(haystack)):
            checkNeedle = haystack[l:r+1]

            if(checkNeedle == needle):
                return l
            
            l += 1
            r += 1

        return -1
        
obj = Solution()
haystack = "abc"
needle = "c"
print(obj.strStr(haystack, needle))