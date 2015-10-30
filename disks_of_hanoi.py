import sys

N = int(sys.argv[1])
print N

a = []
b = [] 
c = []

for i in range(1, N+1):
    a.extend([i])

a.reverse()
print a

def pyramids(a,b,c,N):
    if N > 2:
        print a
        print b
        print c
        pyramids(a,b,c,N-1)
        tmp = a.pop()
        b.extend([tmp])
        pyramids(c,b,a,N-1)
        tmp = b.pop()
        c.extend([tmp])
        pyramids(a,b,c,N-1)
    elif N == 2:
        tmp = a.pop()
        b.extend([tmp])
        tmp = a.pop()
        c.extend([tmp])
        tmp = b.pop()
        c.extend([tmp])
    return

pyramids(a,b,c,N)

print a
print b
print c



