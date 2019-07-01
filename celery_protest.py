import time
from celery import Celery


broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('tasks',broker=broker,backend=backend)


@app.task
def add(x,y):
    print('start call fun')
    time.sleep(4)
    return x+y

if __name__=="__main__":
    print('start task')
    res = add.delay(2,4)
    print('end task')
    print(res)
