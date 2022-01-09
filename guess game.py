guess_num = 9
chances = int(input("enter no.of chances:"))
right=0
wrong=0
for i in range(1,chances+1):
    print(i,"chance")
    n=int(input("enter the number"))
    if n==guess_num:
        print("right")
        right=right+1
    elif n!=guess_num:
        print("wrong")
        wrong=wrong+1
    else:
        print("better luck next time")
print("total chances:",chances),
print("no.of times you right",right)
print("no.of times wrong",wrong)

