    for x in range(min, max):
        if words[x] in data:
            data[words[x]] += 1
        else:
            data[words[x]] = 1