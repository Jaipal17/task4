W= input('\nInput : Please enter a string\n ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print ("\nOutput :\n ",most_frequent(W))


