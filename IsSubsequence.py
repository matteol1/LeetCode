class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)<len(t):
            #t is longer
            s, t = t, s
        #thiw way s is always longer or equal
        r=0
        l=0
        if len(t)==0:
            return True
        while r<len(s):
            if t[l] == s[r]:
                l+=1            
            if l>=len(t):
                return True
            r+=1
        return False
    
sol=Solution()
sol.isSubsequence("","afdavf")