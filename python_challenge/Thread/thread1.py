from threading import Thread, RLock

lock = RLock()


class SyncThread(Thread):
    def __init__(self, num):
        Thread.__init__(self)
        self.num = num



    def run(self):
        with lock:
            print(f"Writing in gathered file sonnets {self.num}.")
            with open(f"data/data_part_{self.num}.txt") as file:
                with open("gather.txt", "a") as gather:
                    gather.write(file.read())
                    gather.write("\n")

open('gather.txt', 'w').close()
for i in range(1, 11):
    test = SyncThread(i)
    test.run()

with open('gather.txt', 'r') as f:
    print(f.read())