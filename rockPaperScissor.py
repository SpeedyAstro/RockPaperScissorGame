import random
#print("\t\t\t ROCK PAPER SCISSOR")

WEAPONS = ['rock', 'paper', 'scissors']

game_rules= {'rock': 'paper','paper': 'scissors','scissors': 'rock'}


def get_winner(user_weapon , computer_weapon):
    if user_weapon == computer_weapon :
        return "TIE , Nobody Won"
    return 'Human' if computer_weapon != get_defeater(user_weapon) else 'Computer'
def get_defeater(weapon) :
    return game_rules[weapon]

def get_user_weapon():
    while True:
        weapon = input("Choose a weapon [Rock , Paper , Scissors] ").lower().strip()

        if weapon in WEAPONS:
            return weapon
        else:
            print("Invalid weapon")
            
def main():
    while True:
        computer_weapon = random.choice(WEAPONS)
        user_weapon = get_user_weapon()

        winner = get_winner(user_weapon,computer_weapon)

        print(f"Computer Chose {computer_weapon}.")
        print(f"Winner is {winner}")

        play_again = input("do you want to play again [y/n]")

        if play_again == 'n' :
            break
        
if __name__ == "__main__":
    main()