from multiprocessing import Pool
import threading
import time


def task(i):
    print('start task {}'.format(i))
    time.sleep(2)
    print('end task {}'.format(i))

#pool = Pool()
#arg = list(range(3))

start = time.time()
tread_list = []
for i in range(3):
    t = threading.Thread(target = task,args = (i,))
    tread_list.append(t)
for t in tread_list:
    t.start()
for t in tread_list:
    t.join()

#pool.map_async(task,arg)
#pool.close()
#pool.join()
end = time.time()
print('runing {}s'.format(end-start))
