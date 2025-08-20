import random

'''
1 for snake 
-1 for water 
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youdict = {"s" : 1, "w" : -1, "g" : 0}
reversedict = {1 : "s", -1 : "w", 0 : "g"}

you = youdict[youstr]

print(f"you chose { reversedict[you]}\n computer chose {reversedict[computer]}")


if((computer - you) == -1 or (computer - you) == 2):
    print("you lose!")
else:
    print("You win!")