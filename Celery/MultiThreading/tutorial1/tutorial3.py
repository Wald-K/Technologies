import threading
import time


class MyThread(threading.Thread):
	def run(self):
		print('{} has started'.format(self.getName()))
		# try:
		# 	if self._target:
		# 		self._target(*self._args, **self._kwargs)
		# finally:
		# 	del self._target, self._args, self._kwargs
		# super().run()
		super(MyThread, self).run()
		print('{} has finished'.format(self.getName()))


def sleeper(n, name):
	print(f'Hi Im {name}. Going to sleep {n} seconds')
	time.sleep(n)
	print(f'{name} woken up')

for i in range(4):
	t = MyThread(target = sleeper, name='Thread {}'.format(i+1),
	 args=(3, 'thread {}'.format(i+1)))
	t.start()







