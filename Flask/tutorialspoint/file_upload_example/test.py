class firstn(object):
    def __init__(self, n):
        self.n = n
        self.num, self.nums = 0, []

    def __iter__(self):
        return self

    # Python 3 compatibility
    # def __next__(self):
    #     return self.next()

    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        # else:
        #     raise StopIteration()


def first(n):
	num = 0
	while num < n:
		yield num
		num += 1

table = [n for n in first(10000)]
print(table)