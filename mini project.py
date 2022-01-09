import random
#r="rock"
#p="paper"
#s="scissor"
Li1=["rock","paper","scissor"]
p1=input("1st player name:")
p2= input("2nd player name:")
q=int(input("number of turns you want to play:"))
us1_points=0
us2_points=0
TIE_P=0
for i in range(1,q+1):
    print(i,"turn")
    user1=input("enter 1st player choice:rock,paper,scissor:")
    Li1=["rock","paper","scissor"]
    user2=random.choice(Li1)
    print("user1 choice:",user1)
    print("user2 choice:",user2)
    if user1==user2: 
        print("TIE")
        TIE_P=TIE_P+1
    elif user1=="rock":
        if user2=="scissor":
            print("user1 wins",user1)
            us1_points=us1_points+1
        else:
            print("user2 wins")
    elif user1=="paper":
        if user2=="scissor":
            print("user2 wins",user2)
            us2_points=us2_points+1
        else:
            print("user1 wins")
    elif user1=="rock":
        if user2=="papper":
            print("user2 wins",user2)
            us2_points=us2_points+1
        else:
            print("user1 wins")
            us1_points=us1_points+1
    else:
        print("invalid")
print("Total of number games:",q)
print("TIE:POINTS:",TIE_P)
print("USER1_POINTS:",us1_points)
print("USER2_POINTS:",us2_points)
if us1_points>=us2_points and us2_points>=TIE_P:
    print("USER1 wins the game !!! Congrats !!!!")
elif us2_points>us1_points:
    print("USER2 wins the game !!! Congrats !!!!")
else:
    print("tie wins")




