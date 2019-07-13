import threading
import time

total = 4

def create_item():
	global total
	for i in range(10):
		time.sleep(2)
		print('item added')
		total += 1
	print('creation is done')

def create_item_2():
	global total
	for i in range(7):
		time.sleep(1)
		print('item added')
		total += 1
	print('creation is done')

def limitor():
	global total
	while True:
		if total > 5:
			print('overloaded')
			total -= total
			print('substracted 3')
		else:
			time.sleep(1)
			print('Waiting for substraction')

creator_1 = threading.Thread(target = create_item)
creator_2 = threading.Thread(target = create_item_2)
limitor = threading.Thread(target = limitor, daemon = True)
# limitor.daemon = True  # to powoduje że nie będzie się wykonywał w kółko tylko zakończy się razem z głównym wątkiem main()
# albo możemy podać podczas tworzenia wątku np. imitor = threading.Thread(target = limitor, daemon = True)



creator_1.start()
creator_2.start()
limitor.start()

# creator_2.join()
# creator_1.join()
# limitor.join()



print('All finished !!!!!!!!!!!!!!!!!1')
print(limitor.isDaemon())










