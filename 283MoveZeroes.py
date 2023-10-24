class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #array=[1,0,3,0,2]
        #output = [1,3,2,0,0]
        i = 0
        while i<len(nums)-1:
            if nums[i]==0:
                j=i+1
                while nums[j]==0 and j<len(nums)-1:
                    j+=1
                #found index of next non zero element
                if j>=len(nums):
                    break
                nums[i]=nums[j]
                nums[j]=0
            i+=1
            print(nums)


#array=[0,1,0,3,0,2,0]
#sol=Solution()
#sol.moveZeroes(array)


class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0 yhefgz
        num_list = []
        counter=0
        while i<len(nums):
            if nums[i]!=0:
                num_list.append(nums[i])
                counter+=1
            i+=1
        print(num_list)
        for _ in range(counter-1):
            num_list.append(0)
        return num_list
    
array=[0,1,0,3,12]
sol2=Solution2()
print(sol2.moveZeroes(array))

