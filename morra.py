#MADE BY: Alfie Antony (Student ID: 22504619) & Zygimantas Gricius (Student ID: 22374196)

import random as r
import math as m

'''
The first thing we implemented into our code was the random and math python modules.
We needed the random module to create a response from the CPU and the math module for calculating whether or not the final answer was even or odd.
'''

spacing = "--------------------------------------------------------------------------"
cpu_msg = "The CPU has selected: "
error_msg = "ERROR: invalid selection!"

player_points = 0
cpu_points = 0

list = [0, 0, 0, 0, 0]
history = []
winner = 0

'''
These are the variables / texts that we created alongside the functions.
The "spacing", "cpu_msg" and "error_msg" texts were created to simplify the code and reduce total characters, making the code easier to see,
creating a text variable also helped as we only needed to edit the text once for it to be implemented across the entire code.

The "player_points" and "cpu_points" were created to store the amount of points the player and the CPU had.

The "list" and "history" arrays were created to store data of the amount of times odd was chosen, the amount of times even was chosen,
the amount of times the player won and lost a round and also the amount of extra points the player receieved. We originally wanted to use
five seperate variables for this, but found that the data didn't always match up to what we manually recorded, so we changed it to a list with five
different integers, representing the variables.

Lastly the "winner" variable is only used in the exitgame() function to exit the while loop, as we could not implement a break statement in the function.
'''

def odd_or_even():
    global ans
    ans = input("Please select odd or even:\n")
    if ans.lower() == "even":
        print("You have selected {}!".format(ans.lower()))
        list[1] = list[1] + 1
    elif ans.lower() == "odd":
        print("You have selected {}!".format(ans.lower()))
        list[0] = list[0] + 1
    else:
        print(spacing)
        print(error_msg)
        odd_or_even()

'''
The first function we wrote was to ask whether the player wanted to be even or odd. The code assigns the "ans" variable to
be a global variable as it is needed in the cpuselect() function. We have an if, elif and else statement which gives three paths
the player can go with their input.

We also increment the odd / even chosen integer by one based on what the user inputs.
'''

def fingerselect():
    print(spacing)
    global fingers
    fingers = input("Please select a number of fingers from 1 to 10:\n")
    if 0 < int(fingers) <= 10:
        print("You have selected: {}".format(fingers))
    
    else:
        print(error_msg)
        fingerselect()

'''
The fingerselect() function asks the user to input the amount of "fingers" they would like to show,
the if statement checks if the user selected a number from 1 to 10 and if they didn't, prints an error text and runs itself again.
'''

def append():
    global list
    history.append(list)
    list = [0, 0, 0, 0, 0]

'''
The append() function was actually the last function we wrote, as we focused on the rest of the game first, leaving the history part to be last.
The function appends the list to the empty history array, and then resets the list.
'''
    
def cpuselect():
    print(spacing)
    global cpu

    cpu = r.randint(1, 10)
    print(cpu_msg + str(cpu))
'''
The cpuselect() function creates a cpu variable that selects a random integer from 1 to 10 and prints the "cpu_msg" text and whatever
number it has randomly chosen.
'''


def summation():
    
    global player_points
    global cpu_points
    print(spacing)
    summation = int(fingers) + int(cpu)
    print("The sum of the fingers equals {}!".format(str(summation)))
    if m.fmod(summation, 2) == 0:
        if ans.lower() == "even":
            print("You win!\nAdding two points...")
            player_points = player_points + 2
            list[2] = list[2] + 1
        else:
            print("You lose!\nCPU wins two points!")
            cpu_points = cpu_points + 2
            list[3] = list[3] + 1
    else:
        
        if ans.lower() == "odd":
            print("You win!\nAdding two points...")
            player_points = player_points + 2
            list[2] = list[2] + 1
        else:
            print("You lose!\nCPU wins two points!")
            cpu_points = cpu_points + 2
            list[3] = list[3] + 1
            
    if (summation - int(fingers)) < (summation - int(cpu)):
        print("You were closer to the sum!\nAwarding one point...")
        player_points = player_points + 1
        list[4] = list[4] + 1
        
    elif (summation - int(fingers)) == (summation - int(cpu)):
        print("Both players chose the same number!\nNo one wins points!")
        
    else:
        print("CPU was closer to the sum!\nAwarding one point...")
        cpu_points = cpu_points+ 1
    print("CPU:", cpu_points)
    print("PLAYER:", player_points)

'''
The summation() function is the most complex function in the python file.
It calculates the summation of the "fingers" and the "cpu" variable together, and then prints whatever the sum is.

The if statement asks if the modulo of the "summation" variable is equal to 0, and if it is, asks if the "ans" variable was even or odd.
This also happens in the else statement, whenever the if statement was false.

The player / CPU gets awarded two points and increments the rounds won / rounds lost integer inside the list by one.

There is also an if statement that awards an extra point based on whoever was closer to the sum, the if statement checks
whether the player was closer to the sum than the cpu and if not, goes to the elif statement that checks if
the player and the CPU are the same distance, i.e. they chose the same number.
If both those statements are false, then the else statement runs, as it can be inferred that the CPU is closer.
'''


def exit_game():
    global winner
    global player_points
    global cpu_points
    if player_points >= 6:
        print("You have won!\nCongratulations!\n\n")
        print(spacing)
        leave = input("Would you like to exit the game? Y/N\n")
        append()
        if leave.lower() == "y":
            winner = winner + 1
        elif leave.lower() == "n":
            player_points = 0
            cpu_points = 0
        else:
            print(error_msg)
            print(spacing)
            exit_game()

    elif cpu_points >= 6:

        print("CPU has won!\nBetter luck next time!\n\n")
        print(spacing)
        leave = input("Would you like to exit the game? Y/N\n")
        append()
        if leave.lower() == "y":
            winner = winner + 1         
        elif leave.lower() == "n":
            player_points = 0
            cpu_points = 0
        else:
            print(error_msg)
            print(spacing)
            exit_game()


'''
The exitgame() function checks whether the player_points or the cpu_points have reached or past six.
Whenever someone gets to the number six or passes it, the function prints a series of texts and runs the append() function.
It also asks the user to input whether or not they want to exit the game.

The if statements check if the user input "y" for yes or "n" for no, if "y" was typed, then the while loop stops, and if not,
resets the points. The else statement prints the error text and runs the exitgame() function again.
'''

while winner == 0:
    odd_or_even()
    fingerselect()
    cpuselect()
    summation()
    exit_game()

'''
The while loop runs based on the "winner" variable and stops whenever "winner" isn't 0.
'''

table = "{:^20s}" + "{:^20s}" + "{:^20s}" + "{:^20s}" + "{:^20s}"

'''
The table text formats the headers and the list integers so that they are spaced across from eachother.
'''
print(table.format("--Odds Chosen--","--Even Chosen--","--Rounds Won--","--Rounds Lost--","--Extra points Received--"))

for prev_games in history:
    print((str(history.index(prev_games)+1)) + "." +
          table.format(str(prev_games[0]),str(prev_games[1]),str(prev_games[2]) , str(prev_games[3]) , str(prev_games[4])))

'''
the for loop runs based on the amount of instances of "prev_games" in history, i.e. the amount of reruns the player does.
The for loop first prints the index of the "prev_games" + 1 to create a number, e.g. 1., 2., 3. and then formats the list integers.
'''
print(spacing)
print("--GAME OVER.--\nGoodbye!")
print(spacing + "\n" + spacing + "\nMADE BY: Alfie Antony (Student ID: 22504619) & Zygimantas Gricius (Student ID: 22374196)")
