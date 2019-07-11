class Node:
    def __init__(self, value):
        self.value = value
        self.__children = []
    
    def __repr__(self):
        return 'Node({})'.format(self.value)

    def add_children(self,item):
        self.__children.append(item)

#    def __iter__(self):
#       return iter(self.__children)

    def dfs(self):
        yield self
        for c in self.__children:
            yield from c.dfs()

root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_children(child1)
root.add_children(child2)
child1.add_children(Node(3))
child1.add_children(Node(4))
child2.add_children(Node(5))

for i in root.dfs():
    print(i)
