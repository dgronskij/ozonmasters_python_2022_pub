import time

# Problem: how to run countup / countdown concurrently
# How to do that without threading?

from collections import deque


async def countup(n):
    for i in range(n):
        print('countup', i)
        await s.sleep(1)


async def countdown(n):
    for i in reversed(range(n)):
        print('countdown', i)
        await s.sleep(1)



class Awaitable:
    def __await__(self):
        yield


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
s.call_soon(countup(3))
s.call_soon(countdown(4))
s.run()


#  def gen():
#      print('started')
#  
#      yield 1
#      print('before 2')
#      yield 2
#      print('exit')
#  
#  g = gen()
#  next(g)
#  next(g)
#  next(g)
