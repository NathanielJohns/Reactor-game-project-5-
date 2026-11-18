play = input("Would you like to play a game with me? y/n ").lower()

if play == "y":
    print("Welcome to my reactor game. Please enjoy my work.")
    use_laser = input("The reactor temperature is rising to 30000°F. Do you use the antimatter laser? y/n ").lower()

    if use_laser == "y":
        print("The reactor temperature is lowering. You made a good decision.")
    elif use_laser == "n":
        print("OH NO! Your reactor blew up. That was a bad idea: don't use the antimatter laser?")
    else:
        print("Please enter y or n.")
        replay=input("The reactor temperature is rising to 30000°F. Do you use the antimatter laser? ").lower()

elif play == "n":
    print("Oh well, maybe next time.")
else:
    print("Please enter y or n.")
    replay=input("Would you like to play a game with me? y/n ").lower()
    
