import csv
import random

data_happy = []
data_love = []
data_sad = []
data_freaky = []
data_concentration = []
data_energetic = []
with open("moodsong.csv", "r") as Moodymusic:
    Moods = csv.reader(Moodymusic, delimiter=',')
    # print(Moods)
    for row in Moods:
        data_happy.append(row[0])
        data_love.append(row[1])
        data_sad.append(row[2])
        data_freaky.append(row[3])
        data_concentration.append(row[4])
        data_energetic.append(row[5])

# print(data_happy[1:16])
# print(data_love[1:13])
# print(data_sad[1:13])
# print(data_freaky[1:11])
# print(data_concentration[1])
# print(data_energetic[1:9])

data = [[data_happy], [data_love], [data_sad], [data_freaky], [data_concentration], [data_energetic]]

data_length = len(data)
# print(data_length)
Song_mood = random.randint(0, data_length - 1)
happy = data_happy[1:16 - 1][Song_mood]
love = data_love[1:13 - 1][Song_mood]
sad = data_sad[1:13 - 1][Song_mood]
freaky = data_freaky[1:11 - 1][Song_mood]
concentration = data_concentration[1]
energetic = data_energetic[1:9 - 1][Song_mood]

smile = ["happy", "good mood"]
heart_eyes = ["loving"]
frowning_face = ["sad", "stress", "numb", "lonely"]
smiling_imp = ["naughty", "mischievous"]
monocle_face = ["focus", "relaxed"]
woman_man_dancing = ["dance"]


def songs():
    if your_mood in smile:
        print(happy)
    elif your_mood in heart_eyes:
        print(love)
    elif your_mood in frowning_face:
        print(sad)
    elif your_mood in smiling_imp:
        print(freaky)
    elif your_mood in monocle_face:
        print(concentration)
    elif your_mood in woman_man_dancing:
        print(energetic)


print("Hello there my friend")
your_mood = input("How's your mood today:-")


def emoji():
    if your_mood in smile:
        print("\U0001F604")
    elif your_mood in heart_eyes:
        print("\U0001F60D")
    elif your_mood in frowning_face:
        print("\u2639\uFE0F")
    elif your_mood in smiling_imp:
        print("\U0001f608")
    elif your_mood in monocle_face:
        print("\U0001f9d0")
    elif your_mood in woman_man_dancing:
        print("\U0001f483", "\U0001f57a")


def mood():
    for MOOD in your_mood.lower().split():
        print(MOOD)
        emoji()
        songs()


mood()
