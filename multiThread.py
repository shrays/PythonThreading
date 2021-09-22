
#https://www.youtube.com/watch?v=StmNWzHbQJU
import threading
import time
import math
from collections import Counter

threadCount = 4
data = {}
words = [open('input.txt', 'r').read()]
words = words[0].split()
length = len(words)
#print("--- LENGTH: %s ---" % length)
#print(words)

n = int(math.floor(length/float((threadCount))))
wordLists = []
for i in range(threadCount):
    if i != threadCount - 1:
        wordLists.append(words[i*n:(i+1)*n])
    else:
        wordLists.append(words[i*n:])

dictionaries = []
for i in range(threadCount):
    bruh2 = {}
    dictionaries.append(bruh2)


def do_text(list, dictionary):
    # min = length/threadCount * i
    # max = length/threadCount * (i+1)
    # if(i == threadCount - 1): 
    #     max = length

    for x in list:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

threads = []
start_time = time.time()
for i in range(threadCount):
    t = threading.Thread(target = do_text(wordLists[i], dictionaries[i]))
    threads.append(t)
print("--- MULTI THREAD: %s seconds ---" % (time.time() - start_time))
for i in range(threadCount):
    threads[i].start()
for i in range(threadCount):
    threads[i].join()

counters = [Counter(dictionary) for dictionary in dictionaries]

ans = Counter()
for counter in counters:
    ans = ans + counter

# print(ans)
