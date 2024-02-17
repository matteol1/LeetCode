class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        d1= set(nums1)
        d2= set(nums2)
        for value in nums1:
            if value in nums2:
                #print(f"counter: {i}")
                if value in d1:
                    d1.remove(value)
                if value in d2:
                    d2.remove(value)
        return [list(d1),list(d2)]
#        d1 = dict([nums1[i] for i in range(len(nums1))])
        #d2 = dict(nums2)


a1=[2,3,1,2,5,7]
a2=[2,3,4,1,2,1]
sol = Solution()
print(sol.findDifference(a1,a2))