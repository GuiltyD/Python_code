from functools import partial

def demo(x,y):
    return x-y
x_list = [1,5,8,8,5,87,3]
sort_list = sorted(x_list,key =partial(demo,y=32))
print(sort_list)
print('hello world')
