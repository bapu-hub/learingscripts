import queue
import time

nameList = ["One", "Two", "Three", "Four", "Five"]

workQueue = queue.Queue(3)

for word in nameList:
    #队列已满，最多等待一秒
    if not workQueue.full():
        workQueue.put(word, block=True, timeout=1)
while not workQueue.empty():
    print(workQueue.get())
    time.sleep(1)
    
