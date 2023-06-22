import random

def start_game_against_the_computer():
    attemps = 0
    print("The computer is choosing a number")
    computer_number = str(random.randrange(1000,10000))
    computer_number_lenght = len(computer_number)
    correct_number = ['X']*computer_number_lenght
    print(computer_number)
    print(computer_number_lenght)
    print(correct_number)
    print("The computer had finish now!!!")
    print("Please player introduce your guess:")
    while True:
        player_number = input("> ")
        if len(player_number) < 4 or len(player_number) > 4:
            print("Please enter a number of 4 digits")
            continue
        for i in range(computer_number_lenght):
            if player_number[i] == computer_number[i]:
                correct_number[i] = player_number[i]
            else:
                attemps +=1
        print(correct_number)
        print(attemps)

"""def start_game_two_players():
    valid_number = False
    attemps = 0
    print("Player 1")
    print("Please player 1 set a number of 4 or 5 digit")
    while valid_number != True:
        guess_number = input("> ")
        guess_number_lenght = len(guess_number)
        if not guess_number.isnumeric():
            print("Please enter a valid value")
        elif guess_number_lenght<4 or guess_number_lenght>5:
            print("Please enter a number of 4 or 5 digit")
        else:
            valid_number = True
    correct_number = ['X']*guess_number_lenght
    print("Player 2 enter your first guess of the number")
    valid_number = False
    while True:
        while valid_number != True:
            player_2_guess = input(">")
            if not player_2_guess.isnumeric():
                print("Please enter a valid value")
            elif len(player_2_guess) != guess_number_lenght:
                print(f"Please enter a number of {guess_number_lenght} digits")
            else:
                valid_number = True    
        for i in range(guess_number_lenght):
            for j in range(guess_number_lenght):
                if player_2_guess[j] == guess_number[i] and j!=i:
                    correct_number[i] = player_2_guess[j]
                else:
                    attemps =+ 1
        print(player_2_guess)
        print(guess_number)
        print(correct_number)
"""

if __name__ == "__main__":
    valid_option = False
    print("Master Mind Game")
    while valid_option != True:
        print("Enter 'C' if you want to play against the computer")
        print("Enter 'P' if you want to play against another player")
        option = input("Chose the option > ").upper()
        match option:
            case 'C':
                print("Against the machine")
                start_game_against_the_computer()
                valid_option = True

            #case 'P':
                #print("Against another player")
                #start_game_two_players()
            case _:
                print("Please introduce a valid option")
