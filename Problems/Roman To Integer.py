from operator import le


class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}
        number = 0;
        previous  = 0;

        for i in s:
            if(previous <  romans[i]):
                number += - (previous*2)            
            number += romans[i]    
            previous = romans[i]    
        return number
