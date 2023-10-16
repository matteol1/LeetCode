class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        while len(num_list)>1:
            new_num = sum([int(num_list[i]) for i in range(len(num_list)) ])
            num_list = list(str(new_num))
        return int(num_list[0])

sol = Solution()
print(sol.addDigits(1023122))