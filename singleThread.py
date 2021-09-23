import time

words = [open('input.txt', 'r').read()]
words = words[0].split()
#print(words)

data = {}
start_time = time.time() # starts time clock
for x in words: # counts word(key) occurences(value) in list to dictionary
    if x in data:
        data[x] += 1
    else:
        data[x] = 1
print("--- SINGLE THREAD: %s seconds ---" % (time.time() - start_time))
#print(data)
