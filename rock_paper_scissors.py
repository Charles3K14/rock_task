from random import choice
R="Rock"
P="Paper"
S="Scissors"
a_list=["R", "P", "S"] #storing cpu options in a list
print("Welcome to my awesome game!\nThis is a game of Rock-Paper-Scissors.\nRock beats Scissors, Scissors beats Paper, Paper beats Rock.")

while True:
    user_input=input("Enter one option- 'R' for rock, 'P' for paper or 'S' for scissors:\n")
    user_input=user_input.upper()
#using user's input to access the variables
    if user_input=="R":
        user_input=R
    elif user_input=="P":
        user_input=P
    elif user_input=="S":
        user_input=S
    else:
        print("Error! Enter a valid option")
        continue
#using a_list to access the variables randomly.
    cpu_input=choice(a_list)
    if cpu_input=="R":
        cpu_input=R
    elif cpu_input=="P":
        cpu_input=P
    elif cpu_input=="S":
        cpu_input=S
#comparing user input and cpu input:
    if user_input==cpu_input:
        print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
        print("It's a tie!")
        continue

    elif user_input==R:
        if cpu_input==P:
            print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
            print("CPU wins!")
            break #game ends at every break

        elif cpu_input==S:
            print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
            print("You win!")
            break

    elif user_input==P:
        if cpu_input==R:
            print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
            print("You win!")
            break

        elif cpu_input==S:
            print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
            print("CPU wins!")
            break

    elif user_input==S:
        if cpu_input==P:
            print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
            print("You win!")
            break

        elif cpu_input==R:
            print("Player ({name_1}):CPU ({name_2})".format(name_1=user_input,name_2=cpu_input))
            print("CPU wins!")
            break
print("Thanks for playing")
