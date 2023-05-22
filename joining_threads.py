import threading

def counter():
    for i in range(100):
        print(threading.current_thread().name + '-' + str(i))

t1 = threading.Thread(target=counter, name="Thread One")
t2 = threading.Thread(target=counter, name="Thread Two" )
t1.start()
t2.start()

# We are blocking main thread until other threads are completed
t1.join()
t2.join()
print("Threads----------- should ----------be -------done")