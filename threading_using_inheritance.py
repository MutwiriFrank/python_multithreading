from threading import Thread


class Counter(Thread):

    def __int__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(100):
            print(self.name + '-' + str(i))


t1 = Counter(name ="Thread1")
t2 = Counter(name = "Thread2")

t1.start()
t2.start()