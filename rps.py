import random


user = (input("Rock Paper or Scissors (Input r,p, or s)"))

if user == "r":
    user = 1 
elif user == "p":
    user = 2
elif user == "s":
    user = 3
else:
    print("Enter a Valid Choice")
int(user) == user
computer = random.randint(1,3)
print(user)

print(computer)
if user == computer:
    print("tie")
elif user == 1  and computer == 2:
    print("Loss")
elif user == 1 and computer == 3:
    print("win")
elif user == 2 and computer == 1:
    print("win")
elif user == 2 and computer == 3:
    print("loss")
elif user == 3 and computer == 1:
    print("loss")
elif user == 3 and computer == 2:
    print("win")

    
    
    


    


