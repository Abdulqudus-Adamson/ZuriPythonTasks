import random  #importing the random module


def comparison(player1, cpu): #a function to compare two options and print a result
    if player1 == "R" and cpu == "S":
        print("player1 wins")
    elif player1 == "P" and cpu == "R":
        print("player1 wins")
    elif player1 == "S" and cpu == "P":
        print("player1 wins")
    else:
        print("cpu wins")


def equals(player1, cpu): #a function to compare if two options are equal
    if player1 == "S" and cpu == "S":
        return True
    if player1 == "R" and cpu == "R":
        return True
    if player1 == "P" and cpu == "P":
        return True


print("options : R for rock, P for paper, S for scissors")
options = ["R", "P", "S"]

while True:
    cpu_choice = random.choice(options)
    player1_choice = input("pick an option: ").upper()
    
    
    if player1_choice not in options:
        print("not amongst option , try again!")
        continue

    if equals(player1_choice, cpu_choice):
        print("it's a tie")
        continue

 
    comparison(player1_choice, cpu_choice)
    break