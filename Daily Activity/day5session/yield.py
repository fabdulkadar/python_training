def myfunc(max):
    for i in range(max):
        yield i
        count+=1
        print("Yielded:", i)

for i in myfunc(5):
    print("Received:", i)
