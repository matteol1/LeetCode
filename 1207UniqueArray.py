import heapq

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        unique_values = dict()
        for entry in arr:
            if entry in unique_values:
                unique_values[entry]+=1
            else:
                unique_values[entry]=1
        print(unique_values.values())
        new_set = set(unique_values.values())
        print(new_set)
        print(len(unique_values))
        print(len(new_set))
        if len(unique_values)!=len(new_set):
            return False
        else:
            return True
    
sol=Solution()
sol.uniqueOccurrences([1,1,2,21,1,12,2,11])
newarr = [1,1,2,21,1,12,2,11]
heapq.heapify(newarr)
print(newarr)
