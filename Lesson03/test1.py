from string import ascii_uppercase
class MyList(list):
    def __iter__(self):
        return MyListIter(self)

class MyListIter(object):
    """ A sample implementation of a list iterator. NOTE: This is just a
    demonstration of concept!!! YOU SHOULD NEVER IMPLEMENT SOMETHING LIKE THIS!
    Even if you have to (for any reason), there are many better ways to
    implement this."""
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

if __name__ == '__main__':
    a = MyList([1, 2, 3, 4, 'python'])
    ia = iter(a)
    print 'type(a): %r, type(ia): %r' %(type(a), type(ia))
    for i in a:
        print i,
