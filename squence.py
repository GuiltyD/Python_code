class Group:
    def __init__(self,company,name,staffs):
        self.company = company
        self.name = name
        self.staffs = staffs

    def __reversed__(self):
        pass

    def __getitem__(self,item):
        if isinstance(item,slice):
            return Group(company = self.company,name = self.name,staffs = self.staffs[item])
        else:
            return Group(company = self.company,name = self.name,staffs = self.staffs[item])
    def __str__(self):
        return 'Group({}),{},{})'.format(self.company,self.name,self.staffs)
a = Group('maomaocompany','maomao',['maomao','doudou','pipi'])
print(a[0:2])

        
