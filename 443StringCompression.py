class Solution:
    def compress(self, chars):
        initial_length = len(chars)
        
        #left pointer, edits to list
        left=0
        #right pointer, runs over entire one
        right=0
        while right < len(chars):
            count=0
            while chars[right]==chars[right+count]:
                count+=1
                if right+count==len(chars):
                    break
                #right+=1

            #after the checks, perform changes in list
            if count>1:
                chars[left]=chars[right]
                left+=1
                count_str = str(count)
                for k, char_count in enumerate(count_str):
                    chars[left+k]=char_count
                left+=len(count_str)
                right+=count
            #last shift of the character before ew iteration
            if count==1:
                chars[left]=chars[right]
                left+=1
                right+=1
        #remove rest of the array
        chars = chars[0:left]
        print(len(chars))
        return len(chars) 
            

s= ['a','a','b','b','a','b']
test = ['a','a','b','b','b','b','b','b','b','b','b','b','c']
sol= Solution()
sol.compress(test)