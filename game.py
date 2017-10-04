import random
import math

def user_choice_from_list(list):
    for counter in range(len(list)):
        print(counter+1, ":", list[counter]["item_name"])
    option = input("Please select one of the options: ")
    return option

player = {
    "name": "Gandalf",
    "hp": 100,
    "mp": 100,
    "lvl": 1,
    "xp": 0,
    "hand_item": {
        "name":"Basic Staff",
        "dmg": 5
    },
    "spells": [
        { "name":'Portal',
          "dmg": 0,
          "cost": 1
        },
        { "name":'Fireball',
          "dmg": 10,
          "cost": 8
        }
    ],
    "wallet": 5
}

potion_list = [
    {
        "item_name": "Small Heath Potion",
        "effect-type": "hp",
        "effect-value": 50,
        "price": 10
    },
    {
        "item_name": "Small Mana Potion",
        "effect-type": "mp",
        "effect-value": 50,
        "price": 10
    },
    {
        "item_name": "Medium Heath Potion",
        "effect-type": "hp",
        "effect-value": 100,
        "price": 15
    },
    {
        "item_name": "Medium Mana Potion",
        "effect-type": "mp",
        "effect-value": 100,
        "price": 15
    },
]

monster_list = []
monster_list.append({
    "name": "Norman",
    "hp": 25,
    "mp": 15,
    "dmg": 1,
    "xp": 5,
    "cash": 5
})
monster_list.append({
    "name": "Sahil",
    "hp": 20,
    "mp": 10,
    "dmg": 1,
    "xp": 1,
    "cash": 9
})
monster_list.append({
    "name": "Cat Destroyer",
    "hp": 50,
    "mp": 30,
    "dmg": 5,
    "xp": 5,
    "cash": 13
})

running = True
while running:
    print("Mega Magical Battle Net")
    print("-----------------------")
    print("1) Create New Game")
    print("2) Load Previous Game")
    print("3) Exit")
    choice = input("Please enter an option: ")

    if choice == "3":
        running = False
    elif choice == "1":
        player["name"] = input("Please Enter Name: ")

        game_running = True
        while game_running:
            print("Mega Magical Battle Net")
            print("-----------------------")
            print("1) Battle")
            print("2) Train")
            print("3) Shop")
            print("4) Exit")
            choice = input("Please enter an option: ")

            if choice == "4":
                game_running = False
            elif choice == "1":
                print("Battle Code Goes Here!!!")
            elif choice == "2":
                monster = monster_list[random.randrange(0,len(monster_list))].copy()
                # loop the battle turns
                battle = True
                while battle:
                    # player goes first
                    # player chooses their attack
                    print("1. Attack with melee weapon")
                    print("2. Attack with spell")
                    choice = input("Please select your attack: ")
                    if choice == "1":
                        # player damages the monster with melee
                        print("You damaged", monster['name'], "for", player["hand_item"]["dmg"])
                        monster["hp"] = monster["hp"] - player["hand_item"]["dmg"]
                    elif choice == "2":
                        # player damages the monster with magic
                        # reduce player MP
                        player['mp'] -= player["spells"][1]["cost"]
                        print("You cast",player["spells"][1]["name"],
                              "which damages", monster['name'], "for", player["spells"][1]["dmg"])
                        monster["hp"] = monster["hp"] - player["spells"][1]["dmg"]
                    # if monster still alive
                    print("Monster has",monster["hp"],"health left")
                    if monster["hp"] > 0:
                        # monster attacks
                        player['hp'] -= monster['dmg']
                        print(monster['name'], " damages you for", monster["dmg"])
                        print("You still have", player['hp'], "left")
                    else:
                        print("You are the winner, go get some chicken!")
                        player['xp'] += monster['xp']
                        player['wallet'] += monster['cash']
                        battle = False
                    # End battle when the player has no hp
                    if player['hp'] <= 0:
                        player['hp'] = 0
                        print("Bad luck, better luck next time...")
                        battle = False
                    # repeat loop
            elif choice == "3":
                in_store = True
                while in_store:
                    #print Menu
                    print("Welcome to Shoppers Wizmart")
                    print("1) Buy Potions")
                    print("2) Buy Weapons")
                    print("3) Buy Spells")
                    print("4) Accessories")
                    print("X) Exit store")
                    choice = input("Please enter your choice: ").lower()
                    if choice == "x":
                        in_store = False
                    elif choice == "1":
                        choice = user_choice_from_list(potion_list)

                        if choice.isdigit():
                            index = int(choice) - 1
                            if index in range(len(potion_list)):
                                potion = potion_list[index].copy()
                        else:
                            print("That was not a valid option")
            else:
                print("Please enter a valid option\nPlease try again")

    elif choice == "2":
        print("Placeholder for actual code")
    else:
        print("Please enter a valid option\nPlease try again")

