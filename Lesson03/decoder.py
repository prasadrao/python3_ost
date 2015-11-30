from string import ascii_uppercase
class alphabator(list):
    def __iter__(self):
        return MyListIter(self)

class MyListIter(object):
    def __init__(self, lst):
        self.lst = lst
        self.i = -1
        self.uppercase = list(ascii_uppercase)
    def __iter__(self):
        return self
    def next(self):
        if self.i<len(self.lst)-1:
            self.i += 1
            if self.lst[self.i] > 0  and self.lst[self.i] <27:
            	return self.uppercase[self.lst[self.i] - 1]
	    else:
                return self.lst[self.i]
        else:
            raise StopIteration
