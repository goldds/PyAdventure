import random, time
# main code for intro and script printing

def script(phrases):
  for line in phrases:
    print(line)
    time.sleep(1)


def adventure_intro():
    

  enemies = ["pirate", "dragon", "troll", "evil fairy", "gorgon"]
  # starting variables
  enemy = random.choice(enemies)
  weapon = "dagger"
  stage = "beginning"


  beginning = ["You find yourself standing in an open field, filled with grass and yellow wildflowers.",
       f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.",
       "In front of you is a house. To your right is a dark cave.",
      "In your hand you hold your trusty (but not very effective) dagger."]


  script(beginning)

  story( weapon, enemy)


# refactoring
def crossroads():
  crossroads = ["Enter 1 to knock on the door of the house.",
        "Enter 2 to peer into the cave.",
        "What would you like to do?"]
  script(crossroads)
  choice = int(input("(Please enter 1 or 2.)"))
  return choice


def house(weapon,enemy):
  house_dagger = ["You approach the door of the house.",
  f"You are about to knock when the door opens and out steps a {enemy}.",
  f"Eep! This is the {enemy}'s house!",
  f"The {enemy} attacks you!",
  "You feel a bit under-prepared for this, what with only having a tiny dagger." ]

  house_sword= ["You approach the door of the house.",
  f"You are about to knock when the door opens and out steps a {enemy}.",
  f"Eep! This is the {enemy}'s house!\nThe {enemy} attacks you!"]

  defeat = ["You do your best...",
  f"but your dagger is no match for the {enemy}.",
  "You have been defeated!"]

  victory = [f"As the {enemy} moves to attack, you unsheath your new sword.",
        "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.",
        f"But the {enemy} takes one look at your shiny new toy and runs away!",
        f"You have rid the town of the {enemy}. You are victorious!"]

  if(weapon == "dagger"):
      script(house_dagger)

  if(weapon == "sword"):
    script(house_sword)

  choice = int(input("Would you like to (1) fight or (2) run away?"))

  # choice
  while(True):


    if ((choice == 1) and (weapon == "dagger")):
    
      script(defeat)
      choice = (input("Would you like to play again? (y/n)")).lower()
      

      
      while(True):


        if (choice == "y"):
          print("Excellent! Restarting the game ...")
          adventure_intro()
          break


        elif(choice == "n"):
          quit()


        else:
          choice = int(input("Please enter y or n."))

    # choice


    if((choice == 1) and (weapon == "sword")):

      scripts(victory)
      choice = (input("Would you like to play again? (y/n)")).lower()

      while(True):

        if (choice == "y"):
          print("Excellent! Restarting the game ...")
          adventure_intro()

        elif(choice == "n"):
          quit()
        
        else:
          choice = int(input("Please enter y or n."))


    # choice
    elif (choice == 2):
      story(weapon, enemy)
      break


    else:
      choice = int(input("Please enter 1 or 2."))


def cave(weapon,enemy):
  print("You peer cautiously into the cave.")


  cave_dagger = ["It turns out to be only a very small cave.",
    "Your eye catches a glint of metal behind a rock.",
    "You have found the magical Sword of Ogoroth!",
    "You discard your silly old dagger and take the sword with you.",
    "You walk back out to the field."]

  cave_sword = ["You've been here before, and gotten all the good stuff.",
   "It's just an empty cave now.",
    "You walk back out to the field."]
  
  if(weapon == "dagger"):

    script(cave_dagger)
    weapon = "sword"
    story(weapon, enemy)
    


  else:
    script(cave_sword)  
    story(weapon, enemy)



# story function this is what runs the story 
def story(weapon, enemy):
# crossroads    
  choice = crossroads()


  while(True):

# house
    if (choice == 1):
      house(weapon,enemy)
      break

# cave
    if(choice == 2):
      cave(weapon,enemy)
      break

    elif(choice not in [1,2]):
      choice = int(input("Please enter 1 or 2."))


adventure_intro()