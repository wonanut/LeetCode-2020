"""
933: number of recent calls
简单题，使用队列即可完成
"""

class RecentCounter(object):

    def __init__(self):
        self.queue = []
        self.left = 0
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        while len(self.queue) > 0 and self.queue[0] + 3000 < t:
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)