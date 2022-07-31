import csv
import sys
import random

print(
    '  _         _         _   ____________   _____              ______________     _________________    ______      ______  ____________')
print(
    ' | \       / \       / | |            \  |   |             /              |   /               \ \   |     \____/     | |            \\')
print(
    ' |  \     /   \     /  | |   _________/  |   |            /     __________|  /     _______     \ \  |                | |   _________/')
print(
    ' |   \   /     \   /   | |  /            |   |           |     /            |     /       \     | | |                | |  /')
print(
    ' |   |  /   _   \  |   | |  \_________   |   |           |    |             |    |         |    | | |     \    /     | |  \_________')
print(
    ' |   | /   / \   \ |   | |   _________|  |   |           |    |             |    |         |    | | |     |\__/|     | |   _________|')
print(
    ' |   |/   /   \   \|   | |  /            |   |           |    |             |    |         |    | | |     |    |     | |  /')
print(
    ' |       /     \       | |  \_________   |   |_________  |     \__________  |     \_______/     | | |     |    |     | |  \_________')
print(
    ' |      /       \      | |            \  |             |  \               |  \                 / /  |     |    |     | |            \\')
print(
    ' |_____/         \_____| |____________/  |_____________|   \______________|   \_______________/_/   |_____|    |_____| |____________/')
print('\n')
print("                                                                   TO")
print('\n')
print('                                                __  __          _____ _____ _____    ___  ')
print('                                               |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print('                                               | \  / |  /  \ | |  __  | || |      | (_) |')
print('                                               | |\/| | / /\ \| | |_ | | || |       > _ < ')
print('                                               | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print('                                               |_|  |_/_/    \_\_____|_____\_____|  \___/ ')

print('\n')
print('\n')

data = []
with open("8ballans.csv", "r") as answers:
    ans = csv.reader(answers, delimiter=",")
    # print(ans)
    for row in ans:
        data.append(row)
# print(data)

db_lenght = len(data)


# print(db_lenght)


def magic_8_ball():
    while True:
        random_ans = random.randint(0, db_lenght - 1)
        _ans = data[random_ans][0]
        Quest = input("Ask me a question or type 'quit' if  you want to exit:-")
        print("\n")
        if Quest.lower().strip() == 'quit':
            sys.exit()
        else:
            Quest.lower().lstrip() == Quest
            print(_ans)


magic_8_ball()
