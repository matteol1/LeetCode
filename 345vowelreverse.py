class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels_to_reverse = list()
        for i in range(len(s_list)):
            if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:
                vowels_to_reverse.append(s_list[i])
                #index of indices is same as index of vaowels
            #use 2 indices on list of indices to reverse
        k=1
        for i in range(len(s_list)):
            if s_list[i] in ['a','e','i','o','u','A','E','I','O','U']:
                s_list[i] = vowels_to_reverse[-k]
                k+=1
        return ''.join(s_list)
    
class1= Solution()
print(class1.reverseVowels("This is a sentence with flipped vowels"))