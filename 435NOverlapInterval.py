class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        #easuer if i sort by first element
        #sort by start, tie end smallest to largest
        intervals.sort()#key=lambda x: x[1]-x[0])
        print(intervals)
        i=1
        tmp_intervals= [intervals[0]]
        while i < len(intervals):
        #for interval in intervals:
            #print(tmp_intervals)
            start = intervals[i][0]
            end  = intervals[i][1]
            #if start is the same as previous start, remove -> keep smallest with same start
            if start==tmp_intervals[-1][0]:
                i+=1
            #if start inside previous interval, remove
            elif start < tmp_intervals[-1][1] and end < tmp_intervals[-1][1]:
                tmp_intervals.pop(-1)
                tmp_intervals.append(intervals[i])
                i+=1
            elif start < tmp_intervals[-1][1]:
                i+=1
            else:
                tmp_intervals.append(intervals[i])
                i+=1
            #need to remove all intervals with that start that have an end within next interval
        #print(tmp_intervals)
        return len(intervals) - len(tmp_intervals)

#Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
#Example 2:
#
#Input: intervals = [[1,2],[1,2],[1,2]]
#Output: 2
#Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
#Example 3:
#
#Input: intervals = [[1,2],[2,3]]
#Output: 0
#Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

test_int = [[1,2],[2,3],[1,4]] 
test_int = [[1,2],[2,3],[3,4],[1,3]]
test_int =  [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]

sol = Solution()
a = sol.eraseOverlapIntervals(test_int)
print(a)