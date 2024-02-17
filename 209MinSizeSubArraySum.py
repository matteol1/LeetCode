class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        partial_sum , i = 0, 0
        while partial_sum<target and i<len(nums):
            partial_sum += nums[i]
            i+=1
        #if no solution
        if partial_sum<target:
            return 0
        current_window=i
        i=0
        while i<len(nums):
            partial_sum -= nums[i]
            if partial_sum >= target:
                current_window -=1
            if i+current_window<len(nums):
                partial_sum += nums[i+current_window]
            i+=1
        #last part of array

        return current_window

test_arr = [1,2,3,4,5]
sol=Solution()
print(sol.minSubArrayLen(15, test_arr))



class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        partial_sum , i = 0, 0
        while partial_sum<target and i<len(nums):
            partial_sum += nums[i]
            i+=1
        #if no solution
        if partial_sum<target:
            return 0
        current_window=i
        i=0
        while i+current_window<len(nums):
            partial_sum -= nums[i]
            if partial_sum >= target:
                current_window -=1
            else:
                partial_sum += nums[i+current_window]
            i+=1
        window_size = current_window
        #last part of array
        while i<len(nums):
            current_window-=1
            partial_sum -= nums[i]
            if partial_sum >= target:
                window_size = current_window
            i+=1
        return window_size
    