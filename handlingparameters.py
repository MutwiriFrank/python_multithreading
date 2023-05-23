import threading

def counter(x):
    for x in range(x):
        print(threading.current_thread().name + '-' + str(x))

t1 = threading.Thread(target=counter, name = 'Thread(1)', args=(10,))
t2 = threading.Thread(target=counter, name = 'Thread(2)', args=(100,))

t1.start()
t2.start()
