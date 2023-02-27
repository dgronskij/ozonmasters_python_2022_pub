import time
import threading

# Problem:
# producer writes into the queue
# consumer reads from the queue

# how to do simultaneously



from collections import deque
from queue import Queue

q = Queue()

def producer():
    for i in range(5):
        print('producer', i)
        q.put(i)
        time.sleep(1)
    q.put(None)  # Sentinel value -- signal to stop


def consumer():
    while True:
        value = q.get()
        if value is None:
            print('consumer exit')
            return
        print('consumer:', value)

    


#  class Scheduler:
#      def __init__(self):
#          self._ready_to_run = deque()
#          self._sleeping = []
#          self._cnt = 0
#  
#      def call_with_delay(self, delay, func):
#          deadline = time.time() + delay
#          t = (deadline, self._cnt, func)
#          self._sleeping.append(t)
#          self._sleeping.sort()
#  
#  
#      def call_soon(self, func):
#          self._cnt += 1
#          self._ready_to_run.append(func)
#  
#      def run(self):
#          # run everything that may be run now
#          # then run those delayed functions that may be run
#          while self._ready_to_run or self._sleeping:
#              if not self._ready_to_run:
#                  # pick functions that must be called first
#                  deadline, _, func = self._sleeping.pop(0)
#                  time.sleep(max(0, deadline - time.time()))
#                  self._ready_to_run.append(func)
#              else:  # we have something that may be run NOW
#                  func = self._ready_to_run.popleft()
#                  func()


threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
