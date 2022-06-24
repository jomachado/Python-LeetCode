class Solution:
    def isValid(self, s: str) -> bool:
        openParenthese = {'(': ')', '{': '}', '[': ']' }
        previousParenthese = []

        if(len(s)%2 !=0):
            return False

        for i in range(len(s)):
            if(s[i] in openParenthese):
                previousParenthese.append(s[i])            
            elif (len(previousParenthese) == 0 or openParenthese[previousParenthese.pop()] != s[i]):
                return False
        return len(previousParenthese) == 0
