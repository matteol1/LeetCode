class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        s=0
        e=len(citations)-1
        h = len(citations)
        index=0
        while s+1<e:
            print(f"s: {citations[s]}, e: {citations[e]}")
            print((e-s)//2, citations[s], e)
            if citations[s + (e-s)//2]>=h:
                e = e - (e-s)//2
            elif citations[s + (e-s)//2]<h:
                h = h - (e-s)//2
                print(h)
                s = s + (e-s)//2
        return h
    
cit = [5,5,6,8,10,12,13]
sol = Solution()
print(f"h-index: = {sol.hIndex(cit)}")
