## More practise necessary?
## Go: http://www.codecademy.com


#example while loop
print "===== Part 1 ====="
index = 1
fruit = 'banana'
while index < len(fruit)+1:
    letter = fruit[-index]
    print letter
    index = index + 1

# example for loop
print "===== Part 2 ====="    
prefixes = 'JKLMOPQ'
suffix = 'ack'

for letter in prefixes:
    print letter + suffix
   
#find a letter in a word...
print "===== Part 3 ====="
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
    
#Program that counts how many a's in the word banana
print "===== Part 4 ====="
word = 'banana'
count = 0
#for letter in word:
if letter == 'a':
    count = count + 1
print count

# for loop
print "===== Part 5 ====="
numbers = [1,2,5]
for num in numbers:
    print num
    
print "Test"
numbers = []
for i in range(0,6):
    numbers.append(i)
print [numbers]

#example function mit return fuer wieder(her)gabe des weres
def convertTemp(temp,targetunit): 
    if targetunit == "C":
        result = 5.0/9 * (temp - 32)
    elif targetunit == "F":
        result = 9.0/5 * temp + 32
    else:
        result = None
    return result
    
tempInC = convertTemp(72,"C")
print tempInC
tempInF = convertTemp(-20,"F")
print tempInF

#example function mit return fuer wieder(her)gabe des weres
#This time, I specified the arguments default values,
#so that they become optional and I dont have to pass them when calling the function
def convertTemp2(temp,targetunit="C"): 
    if targetunit == "C":
        result = 5.0/9 * (temp - 32)
    elif targetunit == "F":
        result = 9.0/5 * temp + 32
    else:
        result = None
    return result
    
tempInC = convertTemp(72,"C")
print tempInC
tempInF = convertTemp(-20,"F")
print tempInF

#You can specify which parameter you pass, by explicitly putting the parameter name in the function call
def drawCircle(pos,radius=5,color="green",alpha=1.0): #function that draws circle
    drawCircle((50,60),color="blue")

#With the command global you can use variables outside of functions
b=5
def printNumber():
    global a
    global b
    a = 3
    print b
    b += 5
    print a
printNumber()
print a

#You can either directly refer to a function like in b or append
def someFunction():
    return 5
a = someFunction()
b = someFunction
print a
print b
print b()

#Just like in LaTeX you have to import certain modules. To do that use import, for all see http://docs.python.org/modindex.html
import math
math.cos()
math.sin()
math.pi
#or importing via an alias
import math as m
m.cos
m.pi
#or specific variables and functions from a module
from math import pi
from math import cos
cos(pi)
#or alias
from math import factorial as f
f(5)