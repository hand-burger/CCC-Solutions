#Get user input, remove white spaces, sort alphabetically and check if equal

first = input('Enter first phrase> ')
second = input('Enter second phrase> ')

first = ''.join(first.split())
second = ''.join(second.split())

if(sorted(first) == sorted(second)):
    print('Is an anagram')
else:
    print('Is not an anagram')