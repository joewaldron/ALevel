import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
  def __init__(self, threadID, name, q):
     threading.Thread.__init__(self)
     self.threadID = threadID
     self.name = name
     self.q = q
  def run(self):
     print ("Starting " + self.name)
     process_data(self.name, self.q)
     print ("Exiting " + self.name)

def process_data(threadName, q):
  while not exitFlag:
     queueLock.acquire()
     if not workQueue.empty():
        data = q.get()
        queueLock.release()
        print ("%s processing %s" % (threadName, data))
        #DO STUFF
        pos = 0
        while pos < len(data):
           if data[pos] == 1:
               data[pos] = 0
               pos += 1
           elif data[pos] == 0:
               data[pos] = 1
               pos += 1
        finish.append(data)
     else:
        queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4","Thread-5"]
nameList = [[1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,0,1],
           [1,1,1,1,1,1,1,1]]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
finish = []
# Create new threads
for tName in threadList:
  thread = myThread(threadID, tName, workQueue)
  thread.start()
  threads.append(thread)
  threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
  workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
  pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
  t.join()
for eachline in finish:
   print(eachline)
print ("Exiting Main Thread")
