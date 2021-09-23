import threading
import time
import math
from collections import Counter

tCount = 4 # Number of Threads
words = [open('input.txt', 'r').read()]
words = words[0].split() # each words gets list index

numSection = int(math.floor(len(words)/float(tCount))) # Calculates workload for each thread
wordsLists = [] 
for i in range(tCount): # partitions words[] into 4 equal lists
    if i != tCount - 1:
        wordsLists.append(words[i*numSection:(i+1)*numSection])
    else:
        wordsLists.append(words[i*numSection:])

dictList = []
for i in range(tCount): # initializes 4 {} into dictList[]
    dictionary = {}
    dictList.append(dictionary)

def do_text(list, dictionary):
    for x in list: # counts word(key) occurences(value) in list to dictionary
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

threads = []
start_time = time.time() # starts time clock
for i in range(tCount):
    t = threading.Thread(target = do_text(wordsLists[i], dictList[i]))
    
    threads.append(t)
print("--- MULTI THREAD: %s seconds ---" % (time.time() - start_time))
for i in range(tCount):
    threads[i].start()
for i in range(tCount):
    threads[i].join()

total = Counter()
for dictionary in dictList: # adds keys of 4 {} in dictList[]
    total = total + Counter(dictionary)
# print(total)
