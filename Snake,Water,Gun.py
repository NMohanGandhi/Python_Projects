import random
print("Welcome to Snake Water Gun game.....................")
user_input = input("Do you want play the Game(yes/no) or exit......")
items = ["snake","water","gun"]
computer_choice = random.choice(items)
#user_choice = input("Choose either snake , gun or water : ").lower()


def game(computer_choice,user_choice):
    global user_input



    if computer_choice==user_choice:

        return None
    elif computer_choice=="snake" and user_choice=="gun":
        return True
    elif computer_choice=="water" and user_choice=="snake":
        return True
    elif computer_choice=="gun" and user_choice=="water":
        return True
    else:
        return False
while True:

    if user_input == "yes":
        user_choice = input("Choose either snake , gun or water : ").lower()
        if user_choice == "snake" or user_choice == "water" or user_choice == "gun":
            print("valid")
            win = game(computer_choice, user_choice)
            print(f"you choose {user_choice} and the computer choose {computer_choice}")
            if win is None:
                print("MAtch Drawn")
                user_input=input("Do you intrested to play game again....(yes/no) or exit")
                #break


            if win == True:
                print("You Won")
                user_input = input("Do you intrested to play game again....(yes/no) or exit ")
                #break

            else:
                print("You lost")
                user_input = input("Do you intrested to play game again....(yes/no) or exit ")
                #break
        else:
            print("invalid")
            user_choice = input("Choose either snake , gun or water : ").lower()

    elif user_input=="no":
        print("Thanks")
        user_input = input("Do you want play the Game(yes/no) or exit")

        #break
    elif user_input=="exit":
        print("! hey thanks for playing...")
        break
    else:
        print("please give either yes or no")
        break









