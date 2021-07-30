inn = '/Users/jack/Documents/CCC-Solutions/CCC 1997/ddc.in'
outt = '/Users/jack/Documents/CCC-Solutions/CCC 1997/ddc.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

# Get first line (number of numbers)
firstLine = fin.readline()
wholeText = fin.readlines()

fin.seek(2)

def search(dictionary, word):
    for i in range(len(dictionary)):
        if dictionary[i] == word:
            return i
    return -1


for i in range(int(firstLine)):
    string = ''
    # Get the string to do some stuff with :3
    for i in range(len(wholeText)):
        nextLine = fin.readline()
        if nextLine == '\n':
            break
        else:
            string += nextLine
    # String acquired, now loop through the words of string & use binary or linear search to compare words to a dictionary
    words = string.split()

    dictionary = [None] * len(words)

    for i in range(len(words)):
        # So for each word in the string array, 
        # 1. Search the dictionary array for any instances of the current word,
        # 1.1 If the current word is found in the dictionary, meaning it is a repeat, then it isn't added to the dictionary
        # 1.2 If the current word is not found in the dictionary, meaning it is a new word, it is added to the end of the dictionary array
        # 2. Once the dictionary is created, meaning every word has been tracked, the loop is done and the None's in the array should be removed
        result = search(dictionary, words[i])
        if result == -1:
            dictionary[i] = words[i]
        else:
            result += 1
            dictionary[i] = result
    print(dictionary)

fin.close()
fout.close()