#if less than 3 just reverse it 
# else:
#add 3 letters at start and end and then take 1st letter to last
#decode:
#if less than 3 just reverse
#else:
#remove 3 letters from start and end
#then remove last letter to start and then take last letter to 1st
import random
import string
z=""
y=""
for i in range(3):
    a=random.choice(string.ascii_letters)
    z=z+a
    b=random.choice(string.ascii_letters)
    y=y+b
word=input("Enter your string")
if len(word)>=3:
    c=word[0]
    word=word.replace(word[0],"")
    coded_word=z+word+c+y
    print(f"your coded word is {coded_word} ")
else:
    coded_word= ''.join(word.__reversed__())

