import logging
import queue
import threading
import time


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker2(x, y=1):
    print(threading.current_thread().getName(), 'start')
    logging.debug(x)
    logging.debug(y)
    time.sleep(5)
    print(threading.current_thread().getName(), 'end')

def worker3():
    logging.debug('start')
    time.sleep(2)
    logging.debug('end')
    
def worker4(d, lock):
    logging.debug('start')
    lock.acquire()
    i = d['x']
    time.sleep(5)
    d['x'] = i + 1
    logging.debug(d)
    lock.release()
    logging.debug('end')

def worker5(d, lock):
    logging.debug('start')
    with lock:
        i = d['x']
        d['x'] = i + 1
        logging.debug(d)
        with lock:
            d['x'] = i + 1
    logging.debug('end')


def worker6(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker7(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker8(semaphore):
    with semaphore:
        logging.debug('start')
        time.sleep(5)
        logging.debug('end')

def worker10(queue):
    logging.debug('start')
    queue.put(100) # [100, 200]
    time.sleep(5)
    queue.put(200) # [100, 200]
    logging.debug('end')

def worker11(queue):
    logging.debug('start')
    #time.sleep(5)
    logging.debug(queue.get())
    logging.debug(queue.get())
    logging.debug('end')

def worker12(queue):
    logging.debug('start')
    while True:
        item = queue.get()
        if item is None:
            break
        logging.debug(item)
        queue.task_done()
    logging.debug('end')

if __name__ == '__main__':
    '''
    #t1 = threading.Thread(name='rename worker1:', target=worker1)
    #t2 = threading.Thread(target=worker2, args=(100,), kwargs={'y': 200})

    t1 = threading.Thread(target=worker1)
    t1.setDaemon(True)
    t3 = threading.Thread(target=worker3)

    t1.start()
    #t2.start()
    t3.start()
    print('stareted')
    t1.join() # Daemon化する場合
    '''

    '''
    #threads = []
    for _ in range(5):
        t = threading.Thread(target=worker1)
        t.setDaemon(True)
        t.start( )
        #threads.append(t)
    #for thread in threads:
    print(threading.enumerate())
    for thread in threading.enumerate():
        if thread is threading.currentThread():
            print(thread)
            continue
        thread.join()
    '''

    '''
    t = threading.Timer(3, worker2, args=(100,), kwargs={'y': 200})
    t.start()
    '''

    '''
    d = {'x': 0}

    #lock = threading.Lock()
    lock = threading.RLock()
    t1 = threading.Thread(target=worker5, args=(d, lock))
    t2 = threading.Thread(target=worker4, args=(d, lock))

    t1.start()
    t2.start()
    '''

    '''
    semaphore = threading.Semaphore(2)
    t1 = threading.Thread(target=worker6, args=(semaphore,))
    t2 = threading.Thread(target=worker7, args=(semaphore,))
    t3 = threading.Thread(target=worker8, args=(semaphore,))

    t1.start()
    t2.start()
    t3.start()
    '''

    '''
    queue = queue.Queue()
    for i in range(10):
        queue.put(i)

    t1 = threading.Thread(target=worker10, args=(queue,))
    #t2 = threading.Thread(target=worker11, args=(queue,))
    t3 = threading.Thread(target=worker12, args=(queue,))

    t1.start()
    #t2.start()
    t3.start()

    queue.join()
    queue.put(None)
    '''

    
    queue = queue.Queue()
    for i in range(100):
        queue.put(i)
    ts = []
    for _ in range(3):
        t = threading.Thread(target=worker12, args=(queue,))
        t.start()
        ts.append(t)
    logging.debug('tasks are not done')
    queue.join()
    logging.debug('tasks are done')
    for _ in range(len(ts)):
        queue.put(None)

    [t.join() for t in ts]