import os
import mmap

def memory_map(filename,access = mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access =access)


size = 10000
with open('data','wb') as f:
    f.seek(size-20)
    f.write(b'hello world')

m = memory_map('data')
m[:11]=b'hello world'
with open('data','rb') as f:
    print(f.read(11))
