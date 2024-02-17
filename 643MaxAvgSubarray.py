class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumk = sum(nums[0:k])
        max_sum = sumk
        for i in range(len(nums)-k):
            print(f"index: {i}")
            sumk = sumk + nums[i+k] - nums[i]
            if sumk > max_sum:
                max_sum = sumk
            print(sumk)
        return max_sum/k
    
test=[0,4,0,3,2]
k=1
sol=Solution()

print(sol.findMaxAverage(test,k))
