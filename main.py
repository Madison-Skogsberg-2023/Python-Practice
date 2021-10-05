def function():
    count = 1
    while count < 10:
        print(count)
        count = count + 1

function()

def count():
    count = 1
    while count < 101:
        print(count)
        count = count + 1

count()

def byFive():
    count = 5
    while count <= 100:
        print(count)
        count = count + 5

byFive()

def toTen():
    count = 1
    count2 = 1
    while count2 <= 10:
        while count <= 10:
            print(count)
            count = count + 1
        count2 = count2 + 1
        count = 1

toTen()

myString = "potato"
#           012345
print(myString[2])
#this prints "t" due to positional value

def lastLetter(w):
    return w[len(w)-1]

print(lastLetter("adslkhgfa"))

def spellingBee(w):
    x = 0
    while x < len(w):
        print(w[x])
        x = x + 1
spellingBee("Hello There")

v = "hubble"
print(v[1])
#this prints the 2nd letter of the array of variable 'v'
#the square brackets are read as 'at position x'

#for loops:
#generally call variables 'i' and imbedded for loops go on through the alphabet
#i is an integer
for i in range(0, 10):
    print(i)
#this prints the numbers 0-9 i.e. all numbers less than 10
#this fuction is identical to:
i = 1
while i < 11:
    print(i)
    i = i + 1
#for loops are for sequential values
#while loops are for integers that are non-sequential

def hasL(w):
    for i in range (0, len(w)):
        print