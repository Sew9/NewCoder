import time

time_limit = 30
start_time = time.time()

brands_name = {"Nike": "JUST DO IT", "Coca-cola": "TASTE THE FEELING",
               "Amazon": "SEE WHERE IT TAKES YOU", "NFL": "THURSDAY NIGHT FOOTBALL",
               "Microsoft": "GAMING FOR EVERYONE", "Volkswagen": "VW",
               "Lego": "BRICK TO THE FUTURE", "Starbucks": "STARBUCKS COFFEE",
               "General Motors": "FIND NEW ROADS", "McDonald\'s": "I'M LOVING IT"}

print("Name a 10 brand before time runs out")


def brand():
    score = 0
    while True:
        brands = input("Type a brand:-")
        for key in brands_name:
            if key == brands:
                print(brands_name[key])
                score = score + 1
        '#time'
        elapsed_time = time.time() - start_time
        print(time_limit - int(elapsed_time))
        if elapsed_time > time_limit:
            print("Done")

            print("You have guess " + str(score))
            break


brand()
