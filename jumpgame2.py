class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        queue = [ (0,0) ]
        goal = len(nums) - 1
        visited = set()
        while queue:
            current = queue.pop(0)
            visited.add( current )
            print(current)
            if current[0] == goal:
                break
            for i in range(current[0]+1,current[0]+1+nums[ current[0] ]):
                if ( i, current ) not in visited:
                    queue.append( (i, current ) )
            print(queue)
            #reached the goal
            #now retrace steps to count
        steps=0
        #print(current[0])
        while current != (0,0):
            steps += 1
            current = current[1]
        return steps


arr = [1,2,1,1,1]
sol= Solution()
print(sol.jump(arr))