import random 
def rock_paper_scissors(user,comp):
    print("Rock,Paper,Scissors")
    print("User's choice=",user)
    print("Comp's choice=",comp)
    if(user=="rock" and comp=="scissors") or (user=="paper" and comp=="rock") or (user=="scissors" and comp=="paper"):
        print("User wins!!")
    elif(user=="scissors" and comp=="rock") or (user=="rock" and comp=="paper") or (user=="paper" and comp=="scissors"):
        print("Comp wins!!")
    elif(user==comp):
        print("Same")
    else:
        print("Invalid choice")

user=input("enter your choice:")
choices=("rock","paper","scissors")
comp=random.choice(choices)
rock_paper_scissors(user,comp)