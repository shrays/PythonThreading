data = {}

# The program will take text file as input.
# 
#You will create a key-value data structure to store data, where each word is a key and the
# number of appearances is the value. You can use a linked list of structure/class to store the data.
# The structure contains three data members: string word, int count, link to the next node. You can
# also use the list structure in Python. This this case, you do not need to have the next node
# member.
# 
# Read each word from the text file. If the word is not in the linked list, insert a new node into the
# linked list and set the count to 1. If the word is already in the linked list, add 1 to the count of the
# word.
# 
# Add all the values for each word in the count of the linked list to obtain the total word count for
# each word in the text file.
# 
# Measure the time by adding time stamp before reading the text file and after computed the sum.

words = [open('input.txt', 'r').read()]
words = words[0].split()
print(words)

for x in words:
    if x in data:
        data[x] += 1
    else:
        data[x] = 1

print(data)


# tfile.close()