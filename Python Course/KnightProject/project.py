class Knight:
    def __init__(self, name, armorColor, weaponType, mountType):
        self.name = name
        self.armorColor = armorColor
        self.weaponType = weaponType
        self.mountType = mountType


# Our initial knights
bob = Knight("bob", "blue", "sword", "feral pig")
dianne = Knight("dianne", "black", "dual axe", "floating pumpkin")
knights = [bob, dianne]


# Call for this when you want to create a knight
def create_knight(knights):
    name = input("What would you like your knight to be named?\n")
    armorColor = input("What color should your armor have?\n")
    weaponType = input("What type of weapon should your knight have?\n")
    mountType = input("What type of mount should your knight have?\n")
    newKnight = Knight(name,armorColor,weaponType, mountType)
    knights.append(newKnight)


# Call a knight and change their data
def change_data(knights):
    print("Which knight would you like to change?\n")
    number = select_knight(knights)
    print("And what would you like to change?\n")
    print("1) Name\n" + "2) Armor Color\n" + "3) Weapon Type\n" + "4) Mount Type\n")
    selection = input("Selection: \n")
    new_value = input("What would you like to change it to?\n")
    try:
        if int(selection) == 1:
            knights[number].name = new_value
            print("Name changed!\n")
        elif int(selection) == 2:
            knights[number].armorType = new_value
            print("Armor color changed!\n")
        elif int(selection) == 3:
            knights[number].weaponType = new_value
            print("Weapon type changed!\n")
        else:
            knights[number].mountType = new_value
            print("Mount type changed!\n")
    except:
        print("Problem changing value. Please try again")


# Show the current knights and select one
def select_knight(knights):
    for i in range(len(knights)):
        print(str(i) + " " + knights[i].name + "\n")
    chosen = int(input("Selection: "))
    return chosen


# Thi is the menu and we make our selection here
def menu(knights_number):
    ## Message
    message = "What would you like to do?\n" 
    + "1. Create a new knight?\n" 
    + "2. Update your knight?\n" 
    + "3. Display current knights?\n" 
    + "0. Exit?\n"

    running = True

    ## Select Default Knight

    while(running):
        print(message)
        try: 
            selection = int(input("Selection input: "))
        except: 
            print("That is an invalid input. Try again!")
            continue

        if(selection == 1):
            create_knight(knights)
            print("\nKnight Created!\n")
            continue

        elif(selection == 2):  
            change_data(knights)
            print("\nKnight Changed")
            continue

        elif(selection == 3):
            for knight in knights:
                print("\nKnight's name: " + knight.name 
                + "\nArmor Color: " + knight.armorColor 
                + "\nWeapon Type: " + knight.weaponType 
                + "\nMount Type: " + knight.mountType 
                + "\n\n")
            continue

        else:
            break


## Here is our function calls to start program
menu(0)