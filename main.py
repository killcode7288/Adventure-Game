import time
import sys
for i in 'Loading....':
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.3)
print("")
print("Darlington's Wild Adventure\n")

name = input("Enter your name to begin: \n")
time.sleep(1)
print(name + " Welcome to Darlington's Wild Adventure!!\n")

for i in 'Level 1 Begins':
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1)
print("")

print("Help Darlington find his lost pet in the woods\n")
time.sleep(1)
print("Hint: Pet was last sighted close to a river.\n")
time.sleep(3)

for i in 'Ready...':
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.5)
print("")


answer = input("You approach a cross-road, would you go (left/right): \n")
if answer.lower() == "left":

    answer = input("You walk fo a while and meet a man, would you (greet/pass)? \n")
    if answer.lower() == "greet":
        print("The man takes you to where he last saw Darlington's pet\n")
        answer = input("You see trails of Darlington's pet, would you (follow/ignore) them? \n")
        if answer.lower() == "follow":
            print("You walk till you approach an old bride, the bride is weak.\n")
            answer = input("Would you (run/walk) to get across? \n")
            if answer.lower() == "run":
                print("You made it across the bridge and find Darlington's Pet\n")
                time.sleep(1)
                print("You did it Here are some coins to help you in your next adventure\n")
            elif answer.lower() == "walk":
                print("The bridge could not hold you so you fall to your death....GAME OVER....\n")
            else:
                print("Invalid input, You lose\n")
        elif answer.lower() == "ignore":
            print("Your search becomes and endless one and u run out of water and die\n")
        else:
            print("\nInvalid input, You lose\n")


    elif answer.lower() == "pass":
        print("The man gets pissed, tracks you down and kills you....Sorry you lose:( \n")
        time.sleep(1)
        print("\nTry again next time\n")

    else:
        print("Invalid input, you lose\n")
elif answer.lower() == "right":
    answer = input("You come across a river would you 'swim' to get across or 'walk' around it? \n")
    if answer.lower() == "swim":
        print("You get eaten by crocodiles...You lose.....\n")
    elif answer.lower() == "walk":
        print("You walk and realise the river could not be crossed so you gave up...You lose..\n")
else:
    print("\ntry again\n")