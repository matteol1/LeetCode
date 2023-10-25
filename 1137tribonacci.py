class Solution(object):
    def tribonacci(self, n, memo={}):
        """
        :type n: int
        :rtype: int
        """
        ##print(n//2 + n%2)
        if n in memo:
            return memo[n]
        if n==2 or n==1:
            return 1
        if n==0: 
            return 0
        memo[n] = self.tribonacci(n-1,memo)+self.tribonacci(n-2,memo)+self.tribonacci(n-3,memo)
        return memo[n]

sol = Solution()
n = int(input("N: "))
print(sol.tribonacci(n))