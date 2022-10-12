import random

def main():           
    choice = input("Roll Dice? (y/n): ")    
    while choice == "y":
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        if dice1 == 1 and dice2 == 1:
            display_output(dice1, dice2, total)
            print("Snake eyes!")
        elif dice1 == 6 and dice2 == 6:
            display_output(dice1, dice2, total)
            print("Boxcars!")
        else:
            display_output(dice1, dice2, total)               
        
        choice = input('Roll again? (y/n): ')
        if choice == "n":
            break 

def roll_dice():
    diceRoll =  random.randint(1, 6)
    return diceRoll

def display_output(dice1, dice2, total):
    print()
    print("Dice 1: ", dice1)
    print("Dice 2: ", dice2)
    print("Total : ", total)
    print()
    
print("Dice Roller\n")
main()