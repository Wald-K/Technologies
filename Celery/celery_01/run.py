from tasks import reverse

a = list()

for i in range(10):
    a.append(reverse.delay(str(i)+str(i+1)+str(i+2)))





