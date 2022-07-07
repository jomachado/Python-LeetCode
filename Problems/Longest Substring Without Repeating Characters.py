    
#Using Index
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        currencySubstring = ""


        for char in s:
            if(char in currencySubstring):
                currencySubstring = currencySubstring[currencySubstring.index(char)+1:]
            
            currencySubstring+= char

            longest = max(longest, len(currencySubstring) )
        return longest


# Using Set
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         longest = 0
#         currencySubstring = set()
#         l = 0


#         for char in s:
#             while(char in currencySubstring):
#                 currencySubstring.remove(s[l])
#                 l+=1
            
#             currencySubstring.add(char)
            

#             longest = max(longest, len(currencySubstring) )
#         return longest

s = "pwwkew"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))