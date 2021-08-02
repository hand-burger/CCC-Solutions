import os
# os is only used for finding a dynamic absolute path to the I/O files

absolute_path = os.path.dirname(os.path.abspath(__file__))

inn = absolute_path + '/ddc.in'
outt = absolute_path + '/ddc.out'

# Open files
fin = open(inn)
fout = open(outt, 'w')

# Get first line (number of numbers)
firstLine = fin.readline()
wholeText = fin.readlines()

# Seek back to line 2 after reading the whole file which brings the pointer to the end of the file
fin.seek(2)

# Reset word count
count = 0

# Linear search
def search(dictionary, word, count):
    # Loop through each element of the string array
    for i in range(len(dictionary)):
        # Check if the current word is in the dictionary already, if it does then return the word counter
        if dictionary[i] == word:
            return count
        # If the current word is a string, meaning another word is found, then increase the count
        elif isinstance(dictionary[i], str):
            # Increase the counter here, because that means the number will increase with each new word added to the dictionary
            count += 1
    # When a new word is found, return -1
    return -1

# Looping through each set of text
for i in range(int(firstLine)):
    # Clear the string for the set of text
    string = ''
    # Get the string to do some stuff with
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
        # 2. Once the dictionary is created, meaning every word has been tracked, the loop is done
        result = search(dictionary, words[i], count)
        # When a new word is found, add it to the dictionary
        if result == -1:
            dictionary[i] = words[i]
        else:
            # Otherwise set the None from the array to the word counter
            result += 1
            dictionary[i] = result
    # Loop through each element of the dictionary and check for ints to make strings
    for i in range(len(dictionary)):
        if isinstance(dictionary[i], int):
            dictionary[i] = str(dictionary[i])
    # Now convert the entire array to be a string
    array_to_string = ' '.join(dictionary)
    print(array_to_string)
    fout.write(array_to_string + '\n')

fin.close()
fout.close()