class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[]
#        ans=[0 for _ in range(n+1)]
#        for i in range(n+1):
#            ans.append(0)
#            k = i
#            while k>=1:
#                if k%2:
#                    ans[i]+=1
#                k=k//2
#        return ans
        ans=[]
        for i in range(n+1):
            ans.append(0)
            k = i
            while k>=1:
                if k & 1:
                    ans[i]+=1
                k = k >> 1
        return ans
sol = Solution()
n=int(input("N: "))
import time
a= time.time()
sol.countBits(n)
b = time.time()
print(b-a)
        