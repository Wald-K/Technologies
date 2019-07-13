import threading
import time


def sleeper(n, name):
	print(f'Hi Im {name}. Going to sleep {n} seconds')
	time.sleep(n)
	print(f'{name} woken up')


if __name__ == '__main__':
	t_1 = threading.Thread(target = sleeper, args = (10, 'Thread_1'))
	t_2 = threading.Thread(target = sleeper, args = (3, 'Thread_2'))
	t_1.start()
	t_2.start()
	
	# t_1.join()
	t_2.join()


	print('Still free')
	print('Always free')