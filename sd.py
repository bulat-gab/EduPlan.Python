# generator
def xRange(limit):
    i = 0
    while i < limit:
        yield i
        i += 1

# iterator
def mRange(limit):
    # myList = [i for i in range(limit)]
    myList = list(range(limit))
    for i in myList:
        yield i

limit = 100
nRange = (i for i in range(limit))

a = ...
print(a)
NotImplemented
__debug__

def method():
