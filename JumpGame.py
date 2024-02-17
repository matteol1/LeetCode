class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        if len(nums)==1:
            return True
        queue = []
        queue.append((0,nums[0]))
        while queue:
            current = queue.pop(-1)
            print(current)
            visited.add(current[0])
            if current[0] == len(nums)-1:
                return True
            #if not true current is max jump
            print(min(current[1]+1,len(nums)-current[0]))
            print(f"possible jump: {current[1]}")
            for j in range(min(current[1]+1,len(nums)-current[0])):
              if current[0]+j not in visited:
                queue.append((current[0]+j, nums[current[0]+j]))
            print(queue)
        return False
    

arr= [2,4,2,3,1]
sol = Solution()
print(sol.canJump(arr))
