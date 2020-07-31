import os
print(os.path.join('usr', 'bin', 'spam'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filenames in myFiles:
    print(os.path.join('c:\\Users/hp/Desktop/python', filenames))

print(os.getcwd())

print(os.path.isabs('C:\\Users\hp\PycharmProjects\HackeRank'))

path = 'c:\\Users/hp/Downloads/things_fall_apart--_full_text.pdf'

print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))

path2 = 'c:\\Users/hp/Desktop/python'
print(os.path.getsize(path2))
print(os.listdir())

print(os.path.exists('d:\\'))

helloFile = open('c:\\Users/hp/Desktop/Hello.txt' , 'r')

content  = helloFile.read()
print(content)

open1 = open('c:\\Users/hp/Desktop/sonnet29.txt', 'r')

open2 = open1.read()

print(open2)


baconFile = open('bacon.txt', 'w')
baconFile.write('Hello World!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content2 = baconFile.read()
print(content2)



import shelve

shelfFile = shelve.open('mydata')
cats = ['Marcellus', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print(shelfFile['cats'])
shelfFile.close()
print(type(shelfFile))

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

import pprint

cats = [{'name': 'Marcellus', 'desc':'Warrior'}, {'name':'Pooka', 'desc':'Fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
fileObj = open('myCats.py', 'r')
content3 = fileObj.read()

print(content3)

import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])