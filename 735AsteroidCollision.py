class Solution:
    def asteroidCollision(self, asteroids):
        i=1
        broken_loop=0
        new_stack = [asteroids[0]]
        while i<len(asteroids):
            if len(new_stack)>0:
                if new_stack[-1]>0:
                    last_sign=1
                else:
                    last_sign=-1
            if len(new_stack)==0:
                last_sign=-1
            print(new_stack[-1])
            if asteroids[i]<0 and last_sign==1:
                test_case = new_stack.pop(-1)
                if test_case>abs(asteroids[i]):
                    new_stack.append(test_case)
                elif test_case==abs(asteroids[i]):
                    pass
                else:
                    while len(new_stack)>0 and new_stack[-1]>0 and new_stack[-1] <= -asteroids[i]:
                        print(new_stack[-1])
                        print("shouldn'y be here")
                        if new_stack[-1] == -asteroids[i]:
                            print("should do thji")
                            new_stack.pop(-1)
                            print(new_stack)
                            broken_loop=1
                            break
                        else:
                            new_stack.pop(-1)
                    #should only do if 
                    if len(new_stack)>0 and broken_loop==0:
                        print("really go home")
                        if new_stack[-1]<0:
                            new_stack.append(asteroids[i])
                            last_sign = -1
                    elif len(new_stack)==0 and broken_loop==0:
                        print("aaaaaahhhh")
                        new_stack.append(asteroids[i])

            else:
                new_stack.append(asteroids[i])
                if asteroids[i]>0:
                    last_sign = 1
            i+=1
            print(new_stack)
        return new_stack
    
my_Arr=[2,-1,1,-2]
sol=Solution()
sol.asteroidCollision(my_Arr)