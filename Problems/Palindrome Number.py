
class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        palindrome = 0

        while(number > 0):
            lastNumber =number % 10
            palindrome = palindrome * 10  + lastNumber
            number = (number-lastNumber)/10

        return palindrome==x



obj = Solution()
print(obj.isPalindrome(121))
