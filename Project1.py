### Coding a Simple Game Zone Activity

name = input("Enter your name : ")

print("Welcome " + name +" to my game.")

game = input("Do you want to play this game? , (yes/no) : ").lower()

if game=="yes":
    print(f"hello {name} You have entered our gamezone , thanks  for participating.")
    select_games = input("Which game are you interested in playing? , (chess/ludo/rummy) : ").lower()

    if select_games=="chess":
        print("You are about to play chess and you have a choice to choose white or black colour . Once the colour is chosen the game begins.....")
    elif select_games=="ludo":
        print("You are about to play ludo and selct your piece colour . Once the colour is chosen the game begins.....")
    elif select_games=="rummy":
        print("We are choosing a opponent match for your online , once your oppenent is ready the game will begin.....")
    else:
        print("The provided game option is not valid , please check your input")
else:
    print("Exiting the gamezone , please comeback if interested to play any games.")


