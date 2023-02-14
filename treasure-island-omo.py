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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nYou wake up and find yourself on an island. You have never been here before. Strange trees and plant life are everywhere.")
direction = input(
    "\nYou are sitting on the edge of a path. Which way are you going to go? 'L' for left or 'R' for right: ").lower()

if direction == "r":
    print("\nYou walk a few yards down the path and fall into a Malayan Man Trap! You die slowly from being skewered by sharpened sticks covered with poison! Game Over")
    exit()
elif direction == "l":
    print("\nYou walk down the path for about a kilometer and discover a waterfall. You are mesmerized by its beauty and decided to go for a swim to clean up in the pool at the bottom of the waterfall.")
elif direction != "r" or direction != "l":
    print("\nYou did not enter a valid response. You die. Game Over.")
    exit()

print("\nYou realize that the path continues of the other side of the river. The water is moving fairly quickly, you might be able to swim over. On your way to the pool, you noticed a boat way up on shore. It would take a long time, and a lot of energy, to drag it to the water.")

boat = input(
    "\nWhat do you do? 'D' to drag the boat to the water or 'S' to swim to the other side? ").lower()

if boat == "s":
    print("\nYou are half way across the river when you feel a very large slimy animal brush up against your torso! You freeze with fright and start to float down the river. In front of you, 2 large menacing eyes appear above the water. The next thing you see, is the throat of the river monster as it swallows you whole! Game Over")
    exit()
elif boat == "d":
    print("\nIt took a lot of energy to drag the boat to the water. When you grabbed the oars to set them up to start rowing, you find some elvish bread. After 2 bites, you feel refreshed!")
elif boat != "d" or boat != "s":
    print("\nYou did not enter a valid response. You die. Game Over.")
    exit()

print("\nYou made it to the other side and continue down the path and deeper into the jungle.")

print("\nAfter about an hour, you come to a clearing. On your right, there is a small stream. On the other side you can see a mango tree covered in fruit. About 200 meters down the side of the creek, you see some aboriginals waving at you to come to them. On your left, you see a cave.")

last = input(
    "\nWhat are you going to do? Go into the 'C'ave, get some 'M'angos or head towards the 'A'boriginals? ").lower()

if last == "m":
    print("\nWhen you get to the tree and pick your first mango, instantly you are surrounded by a pack of Honey Badgers! Their fangs and claws rip the flesh off your bones and start to eat you alive! Game Over")
    exit()
elif last == "a":
    print("\nAs you get closer, the Aboriginals looked friendly and they were smiling. As soon as you shook the hand of the first person, another person sliced both of your achilles tendons! You drop to the ground in immense pain. The Aboriginals then start spearing you to death! Game Over")
    exit()
elif last == "c":
    print("\nAt the end of the short cave you see a large chest. You slowly open the chest and inside you find bars of gold, ornate crowns, gold and silver coins along with goblets infused with very large gems!")
elif last != "c" or last != "m" or last != "a":
    print("\nYou did not enter a valid response. You die. Game Over.")
    exit()
