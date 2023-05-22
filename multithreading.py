import threading

def count_operation():
    for i in range(100):
        print(threading.current_thread().name + str(i))

# # sequential operation
# count_operation()
# count_operation()

# threading
t1 = threading.Thread(target=count_operation, name='t_one')
t2 = threading.Thread(target=count_operation, name='t_two')

t1.start()
t2.start()


























