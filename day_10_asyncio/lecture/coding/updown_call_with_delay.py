import time

# Problem: how to run countup / countdown concurrently
# How to do that without threading?

from collections import deque


def countup(n, current=0):
    if current <= n:
        print('countup', current)


        s.call_with_delay(1, lambda: countup(n, current + 1))

        #  time.sleep(1)  # how not to block here?????
        #  s.call_soon(lambda:countup(n, current + 1))
    #  for i in range(n):
    #      print('countup', i)
    #      time.sleep(1)


def countdown(n):
    if n < 0:
        return
    print('countdown', n)

    s.call_with_delay(1, lambda: countdown(n - 1))

    #  time.sleep(1)
    #  s.call_soon(lambda: countdown(n - 1))
    #  for i in reversed(range(n)):
    #      print('countdown', i)
    #      time.sleep(1)


class Scheduler:
    def __init__(self):
        self._ready_to_run = deque()
        self._sleeping = []
        self._cnt = 0

    def call_with_delay(self, delay, func):
        deadline = time.time() + delay
        t = (deadline, self._cnt, func)
        self._sleeping.append(t)
        self._sleeping.sort()


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
                func = self._ready_to_run.popleft()
                func()

s = Scheduler()
s.call_soon(lambda: countup(3))
s.call_soon(lambda: countdown(4))
s.run()

