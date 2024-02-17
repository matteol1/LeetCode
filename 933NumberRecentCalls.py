class RecentCounter(object):

    def __init__(self, counter=[]):
        self.counter = counter

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counter.append(t)
        i=len(self.counter)-1
        while i>=0 and t-self.counter[i]<=3000:
            print(f"Checking: {self.counter[i]}")
            i-=1
        print(len(self.counter) - i - 1)
        return len(self.counter) - i - 1


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1178)
param_2 = obj.ping(1483)
param_3 = obj.ping(1563)
param_32 = obj.ping(4054)
param_4 = obj.ping(4152)
print(param_3)
print(param_4)


