class Solution:
    def climbStairs(self, n: int) -> int:
        cache = { 1:1, 2:2}

        def climStairstCustom( stemps):
            if(stemps in cache):
                return cache[stemps]
            
            cache[stemps] = climStairstCustom(stemps-1) +climStairstCustom(stemps-2) 
            return cache[stemps]
        
        return climStairstCustom(n) 

obj = Solution()
print(obj.climbStairs(5))