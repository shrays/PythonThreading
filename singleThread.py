import time

data = {}
words = [open('input.txt', 'r').read()]
words = words[0].split()
#print(words)

start_time = time.time()
for x in words:
    if x in data:
        data[x] += 1
    else:
        data[x] = 1
print("--- SINGLE THREAD: %s seconds ---" % (time.time() - start_time))
#print(data)
