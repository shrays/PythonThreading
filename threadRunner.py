import threading
import time
import math
from collections import Counter

# ----- GET DATASET ---------

words = [open('input.txt', 'r').read()]
words = words[0].split() # each word gets list index


# ----- SINGLE THREADING ----

data = {}

single_time = time.time() # starts time clock
for x in words: # counts word(key) occurences(value) in list to dictionary
    if x in data:
        data[x] += 1
    else:
        data[x] = 1
single_time = round(time.time() - single_time, 5)
print("- SINGLE THREAD\t:  %s seconds" % single_time)
# print(data)


# ----- MULTI THREADING -----

tCount = 4 # number of threads
threads = [] # threads
wordsLists = [] # specific list of words for each thread
dictList = [] # list of dictionary for each thread
dictionary = {} # dictionary of wordLists for each thread

numSection = int(math.floor(len(words)/float(tCount))) # Calculates workload for each thread
for i in range(tCount):
    if i != tCount - 1: # partitions words[] into 4 equal lists
        wordsLists.append(words[i*numSection:(i+1)*numSection])
    else:
        wordsLists.append(words[i*numSection:])
    dictList.append(dictionary) # initializes 4 {} into dictList[]

def do_text(list, dictionary):
    for x in list: # counts word(key) occurences(value) in list to dictionary
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

multi_time = time.time() # starts time clock
for i in range(tCount):
    t = threading.Thread(target = do_text(wordsLists[i], dictList[i]))
    threads.append(t)

multi_time = round(time.time() - multi_time,5)
print("- MULTI THREAD\t:  %s seconds" % multi_time)
for i in range(tCount):
    threads[i].start()
    threads[i].join()

total = Counter()
for dictionary in dictList: # adds keys of 4 {} in dictList[]
    total = total + Counter(dictionary)
# print(total)

print("- DIFFERENCE\t:  %s seconds" % (single_time - multi_time))
