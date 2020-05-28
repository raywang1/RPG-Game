###RAY WANG RPG GAME###
from show_map import show_map
from maps import maps
from health import playerHealth, enemyHealthMessage

import copy
import os

options = """
[N] North (Up)
[S] South (Down)
[E] East (Right)
[W] West (Left)
"""
message = "You awake in a mysyterious land"
level = 1
name = input("Please enter your name: ")
os.system("clear")
playerX=3
playerY=3
currentMap = "center_map"
health = 10
inFight = False
attack = 1
canMove = True
inShop = False
money = 0

teleportSquares = [[3,1],[1,3],[5,3],[3,5]]
differentsquares = ["W","S","G"]

while True:



  show_map(currentMap,playerX,playerY)


  #### MESSAGE + INPUT ####
  print(message)
  print("")
  print(playerHealth(health,name,level), end="    ")
  if inFight:
    print(enemyHealthMessage(enemyName,enemyHealth,enemyFullHealth))
  print("")
  print(options)
  choice = input("> ")

  os.system('clear')

  #### MOVEMENT ###
  if [playerX,playerY] in teleportSquares and canMove:
    if currentMap== "center_map":
      if [playerX,playerY] == [3,1] and choice.lower() == "n":
        currentMap = "north_map"
        playerX=3
        playerY=6
      if [playerX,playerY] == [1,3] and choice.lower() == "w":
        currentMap = "west_map"
        playerX=6
        playerY=3
      if [playerX,playerY] == [5,3] and choice.lower() == "e":
        currentMap = "east_map"
        playerX=0
        playerY=3
      if [playerX,playerY] == [3,5] and choice.lower() == "s":
        currentMap = "south_map"
        playerX=3
        playerY=0

      elif currentMap== "north_map":
        if [playerX,playerY] == [3,5] and choice.lower() == "s":
          currentMap = "center_map"
          playerX=3
          playerY=0

      elif currentMap== "west_map":
        if [playerX,playerY] == [5,3] and choice.lower() == "e":
          currentMap = "center_map"
          playerX=0
          playerY=3

      elif currentMap== "east_map":
        if [playerX,playerY] == [1,3] and choice.lower() == "w":
          currentMap = "center_map"
          playerX=6
          playerY=3

      elif currentMap== "south_map":
        if [playerX,playerY] == [3,1] and choice.lower() == "n":
            currentMap = "center_map"
            playerX=3
            playerY=6

  if canMove:
    if choice.lower() == "n" and 1<playerY: playerY-=1
    elif choice.lower() == "s" and playerY<5: playerY+=1
    elif choice.lower() == "e" and playerX<5: playerX+=1
    elif choice.lower() == "w" and 1<playerX: playerX-=1

  ### RESET ###
  message=""
  options=""

  ### CHECK TILE ###
  currentSquare = copy.deepcopy(maps)[currentMap][playerY][playerX]
  if currentSquare in differentsquares:
    if currentSquare == "S":
      if inShop:
        if choice.lower() == "a":
          if money >= 2:
            money -= 2
            attack += 1
          else:
            message += "\nNot enough to buy that"

          options += "\n[A] Upgrade attack by 1 (2$)\n[H] Heal (1$)\n[L] Leave Shop"

        if choice.lower() == "h":
          if money >= 1:
            money -= 1
            health = 9 + level
          else:
            message += "\nNot enough to buy that"

          options += "\n[A] Upgrade attack by 1 (2$)\n[H] Heal (1$)\n[L] Leave Shop"

        if choice.lower() == "l":
          canMove = True
          inShop = False

        else:
          options += "\n[A] Upgrade attack by 1 (2$)\n[H] Heal (1$)\n[L] Leave Shop"

      else:
        if choice.lower() == "b":
          canMove = False
          inShop = True
          message = "\nYour money is " + money
          options += "\n[A] Upgrade attack by 1 (2$)\n[H] Heal (1$)\n[L] Leave Shop"
        else:
          options += "\n[B] Enter shop"

    if currentSquare == "G":
      if not inFight:
        message += "A goblin has attacked you"
        canMove = False
        inFight = True
        enemyName = "Goblin"
        enemyHealth = 4
        enemyFullHealth = 4
        options += "\n[A] Attack the Goblin"

      else:
        if enemyHealth>0:
          if choice.lower()=="a":
            enemyHealth -= attack
            health -= 1

          if enemyHealth<=0:
            message += "You have deafeated the Goblin and recieved 1$"
            money += 1
            level += 1
            canMove=True
            inFight=False



  if canMove:
        options += "\n[N] North (Up)\n[S] South (Down)\n[E] East (Right)\n[W] West (Left)"
