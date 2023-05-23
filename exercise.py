import threading
'''
You have an s string (for example: This is a text). Construct 2 threads - these threads print out every second letter of the string. The first string starts with index 0 (first letter) and the second thread starts with index 1 (second letter). 
So the result should be like this:
First thread outputs: ['T', 'i', ' ' s', 'a', 't', 'x']
Second thread outputs: ['h', 's', 'i', ' ', ' ', 'e', 't']
Good luck!
'''

words ='This is a text'
def words_thread(x):

    for n in range(x, len(words), 2):
        print( threading.current_thread().name +'-'+ words[n])

t1 = threading.Thread(target=words_thread,name="Thread(1)", args=(0,))
t2 = threading.Thread(target=words_thread,name="Thread(2)", args=(1,))
t1.start()
t2.start()
