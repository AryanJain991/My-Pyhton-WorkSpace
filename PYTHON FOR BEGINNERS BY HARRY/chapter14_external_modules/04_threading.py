import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)
    print(f"Thread {num}: Finishing")

Threads = []
for i in range(3): # create 3 threads
    Thread = threading.Thread(target = worker, args = (i,))     
    Threads.append(Thread)
    Thread.start()

for Thread in Threads : # wait for all threads to finish
    Thread.join()
print("all thread completed.")  