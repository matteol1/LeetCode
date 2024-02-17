class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string=[]
        for char in s.lower():
            if char.isalpha():
                new_string.append(char)
        print(new_string)
        i=0
        while i<len(new_string)/2:
            if new_string[i] != new_string[-i-1]:
                return False
            i+=1
        return True

s = "ciaoaica"
sol = Solution()
a = sol.isPalindrome(s)
print (a)