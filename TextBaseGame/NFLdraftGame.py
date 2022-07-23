import csv
import random

data = []
data_two = []
data_three = []
data_four = []
with open("Draftgame.csv", "r") as X:
    draft_word = csv.reader(X, delimiter=',')
    print(draft_word)
    for row in draft_word:
        # print(row[0])
        data.append(row[0])
        data_two.append(row[1])
        data_three.append(row[2])
        data_four.append(row[3])

# print(data)
# print(data_two[0])

# Give us the length of the database (how many items are in the list) to pick items from the list that are too bad. You could have been one of the greats. 
db_length = len(data)
# print(db_length)

'''Since all other data have three indexes except data_two, We can use the same formula for the other '''

# This will generate a random number of the list
# The minus one is used for the index numbers, which start with 0 
random_name = random.randint(0, db_length - 1)

# print(db_length)
# print(random_name)
# This will go to a random entry in column 1 of the database
# https://www.youtube.com/watch?v=_Q9-JdOfwUk
chosen_player = data[random_name]
chosen_coach = data_two[0]
chosen_player2 = data_three[random_name]
chosen_player3 = data_four[random_name]

draft_numbers = [12, 14, 25]
draft_numbers2 = [30, 31, 33]
draft_numbers3 = [36, 38, 40]

db_length_numbers = len(draft_numbers)

random_numbers = random.randint(0, db_length_numbers - 1)

draft_orders = draft_numbers[random_numbers]
draft_orders2 = draft_numbers2[random_numbers]
draft_orders3 = draft_numbers3[random_numbers]

name = input("Before starting what is your fullname:-")

# print(chosen_player)
from time import sleep

print("WELCOME TO DRAFT NIGHT!!!!")
sleep(0.9)
answer = input("Are you ready for your next step? (yes/no):-")
sleep(2)

if answer.lower().strip() == "yes":
    print("Let's get the show on the road")
    sleep(0.6)
    print("....")
    sleep(2)
    print("With the first pick, the Giants selects {}!".format(chosen_player))
    sleep(0.6)
    print("Chooses between Baltimore, Miami or Indiana")
    sleep(0.6)

    while True:
        answer = input("Choose a team:-")
        sleep(2)
        if answer.lower().strip() == "baltimore":  # Note: if Baltimore was written with capt B condition wouldn't work
            print("With the {}".format(draft_orders), "pick Baltimore selects Choose a team {}".format(chosen_player2))
            sleep(2)
            print("My time is going to come, don't worry!")
            sleep(0.7)
            print("You got this, babe")
            sleep(0.7)
        elif answer.lower().strip() == "miami":  # Note: if Miami was written with capt M condition wouldn't work
            print(
                "Miami is considering you.\nThey've been looking for a physical DB like you for a while.\nLet see who they pick. you got this, babe")
            sleep(0.7)
            print("Miami is on the board.")
            sleep(0.7)
            print("With the {}".format(draft_orders2), "pick, Miami selected {}".format(draft_orders3), ".")
            sleep(1)
        elif answer.lower().strip() == "indiana":
            print("Ring!Ring!Ring!!! " * 3)
            sleep(0.7)
            answer = input("Type hello to pick up the phone:-")
            sleep(0.5)
            if answer.lower().strip() == "hello":
                print("Hello, this is coach {}".format(chosen_coach), ",how are you feeling!")
                sleep(0.7)
                print("I'm feeling good, coach!")
                sleep(0.7)
                print("Are you ready to be our future star?")
                sleep(0.7)
                answer = input("(yes/no):-")
                sleep(0.5)
                if answer.lower().strip() == "yes":
                    print("Welcome to our team. I can't wait to see you in our uniform.")
                    sleep(0.5)
                    print("Thank you, coach, I can't wait to start working now")
                    sleep(0.7)
                    break
                elif answer.lower().strip() == "no":
                    print("No!")
                    sleep(0.5)
                    print("Sorry coach! I was saying no to my little nephew. He was trying to grab my phone!")
                    sleep(0.7)
                    print("I'm ready, coach")
                    sleep(0.5)
                    print("Good to hear, son. I'll see you soon")
                    sleep(0.5)
                    print("Hang up!")
                    sleep(0.7)
                    break
                else:
                    print("Please pick yes or no")
                    sleep(1)
            else:
                print("One voicemail message")
                sleep(1)
                break
        else:
            print("Please pick chooses between Baltimore, Miami or Indiana")
            sleep(1)
    print("With the {}".format(draft_orders3), "pick Indiana, selects {}".format(name))
    sleep(2)
else:
    answer.lower().strip() == "no"
    print("That's too bad. You could have been one of the greats.")
    sleep(1)
