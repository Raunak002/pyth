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
word=input("Enter your string= \n ?")
choice=int(input("Enter 1 to encode and 0 to decrypt"))
if choice==1:
    if len(word)>=3:
        c=word[0]
        word=word.replace(word[0],"")
        coded_word=z+word+c+y
        print(f"your coded word is {coded_word} ")
    else:
        coded_word= ''.join(reversed(word))
        print(coded_word)
elif choice ==0:
    if len(word)<3:
        z=reversed(word)
        decrypted=''.join(z)
        print(decrypted)
    else:
        z=word.replace(word[:3],"")
        again=z.replace(word[-3:],"")
        removed_letter=again[-1]
        again2=again.replace(again[-1],"")
        decrypted=removed_letter+again2
        print(decrypted)
