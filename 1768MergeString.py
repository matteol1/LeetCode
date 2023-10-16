class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        list1 = list(word1)
        list2 = list(word2)
        merged_list = []
        i = 0
        while i < len(list1) and i < len(list2):
            #2i 2i+1
            merged_list.append(list1[i])
            merged_list.append(list2[i])
            i+=1
        if i== len(list1) and i==len(list2):
            return ''.join(merged_list)
        elif i==len(list1):
            for k in range(i, len(list2)):
                merged_list.append(list2[k])
            return ''.join(merged_list)
        else:# i==len(list2[i]):
            for k in range(i, len(list1)):
                merged_list.append(list1[k])
            return ''.join(merged_list)
            
sol = Solution()
print(sol.mergeAlternately("asdc","ciao"))