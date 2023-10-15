class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i=0
        initial=0
        final=0
        consecutive_zeroes=0    
        maxflowers = 0
        if len(flowerbed)==1 and flowerbed[0]==0:
            return True    
        while i<len(flowerbed):
            print(f"Zeros: {consecutive_zeroes}")
            if flowerbed[i]==1:
                if initial==1 and consecutive_zeroes>1:
                    if consecutive_zeroes%2==0:
                        maxflowers+=1
                initial=0
                final=0
                if consecutive_zeroes>0:
                    maxflowers+=((consecutive_zeroes -1)//2)
                consecutive_zeroes=0
            if flowerbed[i]==0:
                if i==0:
                    initial=1
                if i==len(flowerbed)-1:
                    final=1
                consecutive_zeroes+=1
            #add 1 if zeros are initial or final  
            if final==1 and consecutive_zeroes>1:
                maxflowers+=((consecutive_zeroes -1)//2)
                if consecutive_zeroes%2==0:
                    maxflowers+=1
            i+=1
        if n<=maxflowers:
            return True
        else:
            return False


test_array = [0,1,1,0,0,0,1,0,0,0,1,0]
#test_array = [1,1,1,1]
#test_array = [1,0,1,0,1,0,1,0,1,0]
test_array = [0]

sol = Solution()
mynumber = sol.canPlaceFlowers(test_array, 3)
print(mynumber)
#2 zeroes output 0 unless initial or final zeroes -> 1
#3 zeroes output 1
#4 zeroes output 1 unless initial or final zeroes
#5 -> 2
#6 -> 2         