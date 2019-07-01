import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item ,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name


q = PriorityQueue()
item1 = (Item('maomao'),5)
print(item1)
item2 = (Item('doudou'),10)
item3 = (Item('maodou'),6)
s = [item1,item2,item3]
for i in s:
    q.push(*i)
print(q._queue)
print(q.pop())
