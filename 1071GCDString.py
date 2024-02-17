import re


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str2)>len(str1):
            str1, str2 = str2, str1
        #j = len(str2)
        for i, char in enumerate(str1):
            if i!=0 and char==str1[0]:
                candidate_str = str1[0:i]
                if len(str1)%len(candidate_str):
                    candidate_str=""
                    continue
                else:
                    multiple = len(str1)//len(candidate_str)
                    tmp_str = ''.join(multiple*candidate_str)
                    if tmp_str == str1:
                        break
    #add case string is single character repeated
        if len(str2)%len(candidate_str):
            return ''
        else:
            multiple2 = len(str2)//len(candidate_str)
        #    tmp_str = ''.join(multiple2*candidate_str)
        #    if tmp_str == str2:
        #        break
#                return candidate_str
        #cgeck if there is a larger candidate str with smaller multiple
        i=2
        while i <= multiple:
            tmp_str1 = ''.join(i*candidate_str)
            print(tmp_str1)
            if multiple%i==0 and multiple2%i==0:
                print(i)
                k=multiple//i
                if ''.join(k*candidate_str) == str2:
                    longest_string = i
            i+=1
        print(longest_string)
        print(multiple, multiple2)
        new_string = ''.join(k*candidate_str)
        return new_string
    #        while str2.find(str1[i:j])==-1:
#            j-=1        
    #if re.search(r"[A-Z]*+", str1):


str1 = "ciaociaociaociao"
str2= "ciaociao"

sol=Solution()
print(sol.gcdOfStrings(str1,str2))

k=1
if len(str2)>len(str1):
    str1, str2 = str2, str1
    #make sure 1 is the longest
if len(str1)%len(str2):
    return ''
multiple = len(str1)//len(str2)
i=0
while i<multiple:
    if str1[i*len(str2), (i+1)*len(str2)]!=str1[i*len(str2), (i+1)*len(str2)]:
        return ''
for i,char in enumerate(str2):
    tmp_str = str2[0:i]
    k=0
    while k<multiple:
        if str1[k*len(str2), (k+1)*len(str2)]!=str1[k*len(str2), (k+1)*len(str2)]:
            return ''
        k+=1
    #if tmp_str == 
    k=1
    while k<len(str2):
        if str2==''.join(k*tmp_str):
            largest_k = k
        k+=1
