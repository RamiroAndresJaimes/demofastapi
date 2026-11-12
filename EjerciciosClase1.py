"""
palabra = input("Put your word Here: ").lower()
pattern = input("Put your pattern Here: ").lower()

if pattern in palabra:
    print("Found")
else:
    print("Not Found")

word = input("Write your word here ").lower()

while True:     #aba  
    character = input("Write Character u want to count ").lower()
    if len(character) > 1:
        print("Just one character allowed")
    else:
        print(word.count(character), end="")
        break
word = input("Write your word here ").lower()

print(word[::-1])

word = input("Write your word here ").lower()
word = word.replace(" ", "")
reverse_word = word[::-1]

if word == reverse_word:
    print('True')
else:
    print('False')

while True:
    number = int(input("Write your number here "))
    if number%2==0:
        print("Even")
    else:
        print("Odd")    

import math

while True:
    radius = float(input("Write your radius here "))
    diameter = radius*2
    circumference = 2*math.pi*radius
    area = math.pi*(radius**2)
    print(round(diameter,2), round(circumference,2), round(area,2))

word = input("Write your word here: ")

frecuency = {}

for char in word:
    if char not in frecuency:
        frecuency[char] = 1
    else:
        frecuency[char]+=1

ans = "Theres no characters that appears exactly once"

for char in word:
    if frecuency[char] == 1:
        ans = char
        break

print(ans)


word = input("put your word here")
word = word.split(" ")
answer = word[::-1]

print(answer)


word = input("Write your word here: ")

def remove_duplicates(text: str) -> str:
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return "".join(result)

print(remove_duplicates(word)) 


word = input("Write your word here: ")
result = "".join(dict.fromkeys(word))

print(result)  


text = input("Write your word here: ") #etsernocleidomastoideoso
pattern = input("Write the other word here: ") #oso

def count_how_many_times(text, pattern):
    pattlen = len(pattern) #3
    result = 0
    for i in range (len(text)-pattlen+1):
        sliced = text[i:i+pattlen]
        print(sliced)
        if sliced == pattern:
            result+=1
    return result

print(count_how_many_times(text, pattern))

{()[]}
"""

text = input("Write your word here: ") #etsernocleidomastoideoso 
countingP = 0
countingB = 0


for char in text:
    if char == '(':
        counting+=1
    if char == ')':
        counting-=1
    if counting < 0:
        break

if counting == 0:
    print("Valid")
else:
    print("Invalid")