class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter=0
        first = s[0:k]
        for char in first:
            if char in ['a','e','i','o','u']:
                counter+=1
        max_counter = counter
        for i in range(len(s)-k):
            if s[i] in ['a','e','i','o','u']:
                counter-=1
            if s[i+k] in ['a','e','i','o','u']:
                counter+=1
            if counter>max_counter:
                max_counter = counter
        return max_counter

string1= 'abciiidef'
k=3
sol=Solution()
print(sol.maxVowels(string1, k))