import queue
import threading
import time
#线程之间共享全局变量
#进程之间不共享
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name, time.ctime(time.time()))
        
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        #不断去获取数据直到队列为空
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get() #从队列中取出一个数
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
#互斥锁，同时只能一个进程使用
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    time.sleep(1)
    threads.append(thread)
    threadID += 1

# 填充队列，将5个名字写入一个队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    print("队中还有剩余%d个消息"%workQueue.qsize())

# 主线程判断是否结束，通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
