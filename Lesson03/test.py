class Counter:
    def __init__(self, lst):
        self.lst = lst
        self.current = 0
        self.high = len(lst)

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            return self.lst[self.current]
            self.current += 1
            print self.current

for c in Counter([3]):
    print c
