import random
print("welcome to password Generator:")
chars='asdfghjwertyuiop!@##$%'
n=int(input("enter no.of passwords you want"))
m=int(input("enter no.of characters for password"))
for i in range(n):
    passwords=' '
    for c in range(m):
        passwords+= random.choice(chars)
    print(passwords)
    
