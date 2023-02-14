print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

direction = input(
    "You first come to a fork in the road. The left goes towards a river and the right heads into the bush. Which way to do want to travel? 'left' or 'right'? ").lower()

if direction == "left":
    river = input(
        "\nWhen you get down to the river, you find an old boat. Do you take the 'boat' or will you 'swim'? ").lower()
    if river == "swim":
        cave = input("\nYou get taken down river by the current and end up at the mouth of a cave. Do you go into the 'cave' or do you walk down the 'bank' exploring? ").lower()
    else:
        print("\nWhen you get half-way across, you noticed the boat has been filling up with water! Out of fear, you hang onto the boat and go down with it, drowning.")
    if cave == "cave":
        treasure = input(
            "\nAt the back of the cave you find two treasure chests. A darker than midnight black chest and a glowing chest. Do you open the 'dark' or the 'glowing' chest? ").lower()
    else:
        print("Aboriginals jump out right in front of you, fill your torso with arrows and slice your head off. They take your body back to their camp and eat every piece of your raw flesh")
    if treasure == "dark":
        print("\nCongradulations! You found enough gold and jewels to buy what ever you want! The crown you put on your head teleported you back home before the aboriginals found you!")
    else:
        print("The chest is filled with plutonium and nuclear waste! The only thing protecting you was the sealed chest. You die a horrible death while your skin melts off your bones!")
else:
    print("\nAn Albatros silently swoops down out of the sky, takes you to its nest where it devours you!")
