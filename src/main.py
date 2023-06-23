import random

def start_game_against_the_computer():
    attemps = 0
    count = 0
    print("The computer is choosing a number")
    computer_number = str(random.randrange(1000,10000))
    computer_number_lenght = len(computer_number)
    correct_number = ['X']*computer_number_lenght
    print("The computer had finish now!!!")
    print("Please introduce your guess:")
    while ''.join(correct_number) != computer_number:
        attemps += 1
        count = 0
        player_number = input("> ")
        if len(player_number) < 4 or len(player_number) > 4:
            print("Please enter a number of 4 digits")
            continue
        for i in range(computer_number_lenght):
            if player_number[i] == computer_number[i]:
                correct_number[i] = player_number[i]
                count += 1
            else:
                continue
        print(f"You did get {count} corrects numbers")
        print("Your progress is: ")
        print(*correct_number)
    if ''.join(correct_number) == computer_number:
        print("Congratulations you are a Master Mind!!!")
        print(f"It took you {attemps} tries!")

def validate_input(player_input):
    if not player_input.isnumeric():
            print("Please enter a valid value")
            return False
    elif len(player_input) < 4 or len(player_input) > 4:
            print("Please enter a number of 4 digits")
            return False
    else:
        return True
def win_message():
    print("Congratulation you WON, you are a Master Mind!!!")
    exit(0)  
  
def start_game_two_players():
    valid_number = False
    attemps_player_1 = 0
    attemps_player_2 = 0
    count = 0
    print("Please player 1 set a number of 4")
    while valid_number != True:
        player_1_guess = input("> ")
        guess_number_lenght = len(player_1_guess)
        valid_number = validate_input(player_1_guess)

    correct_number = ['X']*guess_number_lenght
    print("Player 2 enter your guess.")
    
    while ''.join(correct_number) != player_1_guess:
        attemps_player_2 += 1
        count = 0
        player_2_guess = input(">")
        valid_number = validate_input(player_2_guess)
        print(attemps_player_2)
        if valid_number == False:
            continue
        elif  player_2_guess == player_1_guess and attemps_player_2 == 1:
            win_message()
 
        for i in range(guess_number_lenght):
            if player_2_guess[i] == player_1_guess[i]:
                correct_number[i] = player_2_guess[i]
                count += 1   
            else:
                continue
        if count == 0:
            print("None of the numbers in your input match.")
        else:
            print(f"You did get {count} corrects numbers")
            print("Your progress is: ")
            print(*correct_number)

    if ''.join(correct_number) == player_1_guess:
        print(f"It took you {attemps_player_2} tries!")
    print("-"*20)
    print("Now is turn of player 1 to guess")
    print("Please player 2 set a number of 4")
    valid_number = False
    while valid_number != True:
        player_2_guess = input("> ")
        guess_number_lenght = len(player_2_guess)
        valid_number = validate_input(player_2_guess)
    
    correct_number = ['X']*guess_number_lenght
    print("Player 1 enter your guess.")

    while ''.join(correct_number) != player_2_guess:
        attemps_player_1 += 1
        count = 0
        player_1_guess = input(">")
        valid_number = validate_input(player_1_guess)
        if valid_number == False:
            continue
        elif player_1_guess == player_2_guess and attemps_player_1 == 1:
            win_message()

        for i in range(guess_number_lenght):
            if player_1_guess[i] == player_2_guess[i]:
                correct_number[i] = player_1_guess[i]
                count += 1   
            else:
                continue
        if count==0:
            print("None of the numbers in your input match.")
        else:
            print(f"You did get {count} corrects numbers")
            print("Your progress is: ")
            print(*correct_number)
    if ''.join(correct_number) == player_2_guess:
        if attemps_player_1 < attemps_player_2:
            print("Player 1 wins.Congratulation you are a Master Mind!!!")
            print(f"It took you {abs(attemps_player_2-attemps_player_1)} less tries than Player 2!")
            exit(0)
        else:
            print(f"Player 2 wins, to player 1 took {abs(attemps_player_2-attemps_player_1)} more than you.Congratulation you are a Master Mind!!!")
            exit(0)

if __name__ == "__main__":
    valid_option = False
    print("MASTER MIND GAME!!!!!")
    print("""
    Rules of the game
        1.Two players play the game against each other; let’s assume Player 1 and Player 2.
        2.Player 1 plays first by setting a multi-digit number.
        3.Player 2 now tries his first attempt at guessing the number.
        4.If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
        5.The game continues till Player 2 eventually is able to guess the number entirely.
        6.Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
        7.If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
        8.If not, then Player 2 wins the game.
        9.The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons.
    """)
    print("-"*20)
    while valid_option != True:
        print("Enter 'C' if you want to play against the computer")
        print("Enter 'P' if you want to play against another player")
        option = input("Chose the option > ").upper()
        match option:
            case 'C':
                print("Against the machine")
                print('\n')
                start_game_against_the_computer()
                valid_option = True

            case 'P':
                print("Against another player")
                print('\n')
                start_game_two_players()
                valid_option = True
            case _:
                print("Please introduce a valid option")
