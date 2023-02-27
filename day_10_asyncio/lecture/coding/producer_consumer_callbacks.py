import time
import threading

# Problem:
# producer writes into the queue
# consumer reads from the queue

# how to do simultaneously



from collections import deque
from queue import Queue


class Awaitable:
    def __await__(self):
        yield


class AsyncQueue:
    def __init__(self):
        self._q = deque()
        self._waiting = deque()

    def put(self, value):
        self._q.append(value)
        if self._waiting:
            s._ready_to_run.append(self._waiting.popleft())

    
    async def get(self):
        if not self._q:
            self._waiting.append(s._current_gen)
            s._current_gen = None
            await s.switch()
            
        return self._q.popleft()


q = AsyncQueue()

async def producer():
    for i in range(5):
        print('producer', i)
        q.put(i)
        await s.sleep(1)
    q.put(None)  # Sentinel value -- signal to stop


async def consumer():
    while True:
        value = await q.get()
        if value is None:
            print('consumer exit')
            return
        print('consumer:', value)
    


class Scheduler:
    def __init__(self):
        self._ready_to_run = deque()
        self._sleeping = []
        self._cnt = 0
        self._current_gen = None

    async def switch(self):
        await Awaitable()

    async def sleep(self, delay):
        # we are in generator (that is bookkept in self._current_gen)
        deadline = time.time() + delay
        self._cnt += 1 
        t = (deadline, self._cnt, self._current_gen)
        self._sleeping.append(t)
        self._sleeping.sort()
        self._current_gen = None
        await self.switch()


    def call_soon(self, func):
        self._cnt += 1
        self._ready_to_run.append(func)

    def run(self):
        # run everything that may be run now
        # then run those delayed functions that may be run
        while self._ready_to_run or self._sleeping:
            if not self._ready_to_run:
                # pick functions that must be called first
                deadline, _, func = self._sleeping.pop(0)
                time.sleep(max(0, deadline - time.time()))
                self._ready_to_run.append(func)
            else:  # we have something that may be run NOW
                self._current_gen = self._ready_to_run.popleft()
                try:
                    self._current_gen.send(None)
                    if self._current_gen:
                        self._ready_to_run.append(self._current_gen)
                except StopIteration:
                    pass


s = Scheduler()
s.call_soon(consumer())
s.call_soon(producer())
s.run()
