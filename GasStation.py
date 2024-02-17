class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
     #   for start_station in range(len(gas)):
     #       tank = 0
      #      first=1
       #     for i in range(start_station, start_station+len(gas)+1):
      #          tank = tank + gas[i%len(gas)] - cost[i%len(gas)]
       #         print(f"Start: {start_station}, Tank: {tank}")
        #        if tank < 0:
         #           break
          #      print(f"Current: {i%len(gas)}")
           #     if i%len(gas) == start_station and first!=1:
            #        return start_station
             #   first=0
        #return -1

        tank=0
        total = []
        for i in range(len(gas)):
            total.append( (i, gas[i] - cost[i]) )
        print(total)
        total.sort(key = lambda x: x[1])
        print(total[-1])
        start_station = total[-1][0]-1
        first=1
        for i in range(start_station,start_station+len(gas)+1):
            tank = tank + gas[i%len(gas)] - cost[i%len(gas)]
            print(f"Start: {start_station}, Tank: {tank}")
            if tank < 0:
                break
            print(f"Current: {i%len(gas)}")
            if i%len(gas) == start_station and first!=1:
                return start_station
            first=0
        return -1


gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol = Solution()
print(sol.canCompleteCircuit(gas,cost))


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) - sum(cost) < 0:
            return -1
        start = 0
        total = 0
        for i, this_gas in enumerate(gas):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i+1
        return start
    
    