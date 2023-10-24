class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        net_altitude = [0, gain[0]]
        for i in range(1,len(gain)):
            net_altitude.append(gain[i] + net_altitude[-1])
        return max(net_altitude)
    
sol = Solution()
gain = [1,2,1,-3,-2,4,-2,1,-4,7,-4]
print(sol.largestAltitude(gain))

