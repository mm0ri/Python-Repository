import sys
n = int(sys.argv[1])
#n = 73

def processing(n):
    i = 1
    while i <= n:
        if i % 2 == 1 and n % i == 0:
            print(i)
        i += 1

processing(n)