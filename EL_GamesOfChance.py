import random
#Write your game of chance functions here
#OPTION1 (HAT)
def heads_or_tails(guess, bet):
    right_answer_number=random.randint(1,2)
    print("Your guess was: {0}".format(guess))
    if right_answer_number==1:
        right_answer="Heads"
        print("The right answer was: {0}".format(right_answer))
    else:
        right_answer="Tails"
        print("The right answer was: {0}".format(right_answer))
    if guess==right_answer:
        print("You won {0}!".format(bet))
        return bet
    else:
        print("You lost {0}!".format(bet))
        return-bet
#OPTION2 (CH)
def cho_han(guess, bet):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_sum=dice1+dice2
    print("Your guess was: {0}".format(guess))
    if dice_sum%2==0:
        print("The answer was: Even")
    else:
        print("The answer was: Odd")
    if dice_sum%2==0:
        odd_or_even="Even"
    else:
        odd_or_even="Odd"
    if guess==odd_or_even:
        print("You won {0}!".format(bet))
        return bet
    else:
        print("You lost {0}!".format(bet))
        return -bet
#OPTION3 (PAC)
def pick_a_card(bet):
    card_deck=[]
    for i in range(1,5):
        for j in range(1,14):
            card_deck.append(j)
    guess=random.randint(1,13)
    if guess==1:
        guess_name="Ace"
    elif guess==11:
        guess_name="Jack"
    elif guess==12:
        guess_name="Queen"
    elif guess==13:
        guess_name="King"
    else:
        guess_name=guess
    print("You got: {0}".format(guess_name))
    guess_place=card_deck.index(guess)
    card_deck.pop(guess_place)
    counter_choice=random.choice(card_deck)
    if counter_choice==1:
        counter_choice_name="Ace"
    elif counter_choice==11:
        counter_choice_name="Jack"
    elif counter_choice==12:
        counter_choice_name="Queen"
    elif counter_choice==13:
        counter_choice_name="King"
    else:
        counter_choice_name=counter_choice
    print("Your counterpart got: {0}".format(counter_choice_name))
    if guess>counter_choice:
        print("You won {0}!".format(bet))
        return bet
    elif guess<counter_choice:
        print("You lost {0}!".format(bet))
        return -bet
    else:
        print("It's a tie!")
        return 0
#OPTION4 (R)
def roulette(guess, guess_type, bet):
    print("Your guess was: {0}".format(guess))
    choice_possibilities=[]
    for i in range(0, 37):
        choice_possibilities.append(chr(i))
    choice_possibilities.append('00')
    counter_choice=random.choice(choice_possibilities)
    if counter_choice=='00':
        print("The right answer was: 00")
    else:
        print("The right answer was: {0}".format(ord(counter_choice)))
    if guess_type=="EOD":
        if counter_choice=='00' or counter_choice=='0':
            print("You lost {0}!".format(bet))
            return -bet
        elif ord(counter_choice)%2==0 and guess=="Even":
            print("You won {0}!".format(bet))
            return bet
        elif ord(counter_choice)%2==1 and guess=="Odd":
            print("You won {0}!".format(bet))
            return bet
        else:
            print("You lost {0}!".format(bet))
            return -bet
    else:
        if counter_choice=='00' or counter_choice=='0':
            print("You lost {0}!".format(bet))
            return -bet
        elif counter_choice==guess:
            print("You won {0}!".format(35*bet))
            return 35*bet
        else:
            print("You lost {0}!".format(35*bet))
            return -35*bet
#HELPER FUNCTION 1
def correct_type_of_guess_even_odd():
    print("Enter your guess: (Even/Odd)")
    user_guess=input()
    user_guess.lower()
    user_guess.capitalize()
    answer_ok_again_1 = False
    while not answer_ok_again_1:
        if user_guess=="Even" or user_guess=="Odd" or user_guess=="even" or user_guess=="odd" or user_guess=="ODD" or user_guess=="EVEN":
            answer_ok_again_1=True
        else:
            print("Invalid input!")
            print("Enter your guess: (Even/Odd)")
            user_guess=input()
    return user_guess
#HELPER FUNCTION 2
def correct_type_of_guess_heads_tails():
    print("Enter your guess: (Heads/Tails)")
    user_guess=input()
    user_guess.lower()
    user_guess.capitalize()
    answer_ok_again_1 = False
    while not answer_ok_again_1:
        if user_guess=="Heads" or user_guess=="Tails" or user_guess=="heads" or user_guess=="tails" or user_guess=="HEADS" or user_guess=="TAILS":
            answer_ok_again_1=True
        else:
            print("Invalid input!")
            print("Enter your guess: (Heads/Tails)")
            user_guess=input()
    return user_guess
#HELPER FUNCTION 3
def correct_type_of_guess_roulette():
    print("Enter your guess: (1-36)")
    user_guess=int(input())
    answer_ok_again_1 = False
    while not answer_ok_again_1:
        if type(user_guess)==int:
            if user_guess>0 or user_guess<37:
                answer_ok_again_1=True
            else:
                print("Invalid input!")
                print("Enter your guess: (1-36)")
                user_guess=int(input())
                
        else:
            print("Invalid input!")
            print("Enter your guess: (1-36)")
            user_guess=int(input())
    return user_guess
#HELPER FUNCTION 4
def correct_type_of_bet():
    print("Enter your bet:")
    user_bet=int(input())
    answer_ok_again_1 = False
    while not answer_ok_again_1:
        if type(user_bet)==int:
            if user_bet>0:
                answer_ok_again_1=True
            else:
                print("Invalid input!")
                print("Enter your bet:")
                user_bet=int(input())
        else:
            print("Invalid input!")
            print("Enter your bet:")
            user_bet=int(input())
    return user_bet
#Call your game of chance functions here
#Main function for playing one of the previous games
def play_games():
    money = 100
    play_again=True
    while play_again:
        def first_questions():
            print("Which game would you like to play?")
            print("Option 1: Heads or Tails (HOT)")
            print("Heads or Tails")
            print("The idea is to try to choose the correct answer (Heads/Tails)")
            print("You can choose either Heads or Tails")
            print("If you bet 5 credits and choose correctly, you get 5 credits")
            print("If you bet 5 credits and choose wrongly, you loose 5 credits")
            print("Enter (HOT) to choose Option 1")
            print("Option 2: Cho-Han (CH)")
            print("Cho-Han")
            print("The idea is to try to choose correctly if the sum of two dice will be Even/Odd")
            print("You choose either Even or Odd")
            print("If you bet 5 credits and choose correctly, you get 5 credits")
            print("If you bet 5 credits and choose wrongly, you loose 5 credits")
            print("Enter (CH) to choose Option 2")
            print("Option 3: Pick a Card (PAC)")
            print("Pick a Card")
            print("You are automatically given a card (Ace, 2-10, Jack, Queen, King).")
            print("Your counterpart also gets a card from the same deck.")
            print("You win if your card is bigger than the card belonging to your counterpart")
            print("You choose the amount of credits you want to bet")
            print("If you bet 5 credits and choose correctly, you get 5 credits")
            print("If you bet 5 credits and choose wrongly, you loose 5 credits")
            print("Enter (PAC) to choose Option 3")
            print("Option 4: Roulette (R)")
            print("Roulette")
            print("Two game types: Even or Odd and Specific Number")
            print("Enter (R) to choose Option 4")
            print("Enter (EXIT) to exit the game")
        first_questions()
        user_answer=input()
        user_answer.upper()
        answer_ok = False
        while not answer_ok:
            if user_answer=="HOT" or user_answer=="CH" or user_answer=="PAC" or user_answer=="R" or user_answer=="EXIT":
                answer_ok=True
            else:
                print("Invalid input!")
                first_questions()
                user_answer=input()
        if user_answer=="HOT":
            final_user_guess=correct_type_of_guess_heads_tails()
            final_user_bet=correct_type_of_bet()
            if money-final_user_bet>=0:
                money+=heads_or_tails(final_user_guess, final_user_bet)
                print("You now have {0} credits left".format(money))
            else:
                print("You are out of funds! Try choosing another game!")
        elif user_answer=="CH":
            final_user_guess=correct_type_of_guess_even_odd()
            final_user_bet=correct_type_of_bet()
            if money-final_user_bet>=0:
                money+=cho_han(final_user_guess, final_user_bet)
                print("You now have {0} credits left".format(money))
            else:
                print("You are out of funds! Try choosing another game!")
        elif user_answer=="PAC":
            final_user_bet=correct_type_of_bet()
            if money-final_user_bet>=0:
                money+=pick_a_card(final_user_bet)
                print("You now have {0} credits left".format(money))
            else:
                print("You are out of funds! Try choosing another game!")
        elif user_answer=="R":
            dont_get_back=True
            while dont_get_back:
                def second_questions():
                    print("Which game type would you like to play?")
                    print("Option 1: Ever or Odd (EOD)")
                    print("Even or Odd")
                    print("You loose automatically if 0 or 00 gets selected")
                    print("You win if you choose correctly that the selected number (1-36) is Even/Odd")
                    print("If you bet 5 credits and choose correctly, you get 5 credits")
                    print("If you bet 5 credits and choose wrongly, you loose 5 credits")
                    print("Enter (EOD) to choose Option 1")
                    print("Option 2: Specific Number (SN)")
                    print("Specific Number")
                    print("You loose automatically if 0 or 00 gets selected")
                    print("You win if you choose the selected number (1-36) correctly")
                    print("If you bet 5 credits and choose correctly, you get 35*5=175 credits")
                    print("If you bet 5 credits and choose wrongly, you loose 35*5=175 credits")
                    print("Enter (SN) to choose Option 2")
                    print("Enter (BACK) to get back")
                second_questions()
                user_game_type=input()
                user_game_type.upper()
                answer_ok_again = False
                while not answer_ok_again:
                    if user_game_type=="EOD" or user_game_type=="SN" or user_game_type=="BACK":
                        answer_ok_again=True
                    else:
                        print("Invalid input!")
                        second_questions()
                        user_game_type=input()
                if user_game_type=="EOD":
                    final_user_guess=correct_type_of_guess_even_odd()
                    final_user_bet=correct_type_of_bet()
                    if money-final_user_bet>=0:
                        money+=roulette(final_user_guess, user_game_type, final_user_bet)
                        print("You now have {0} credits left".format(money))
                    else:
                        print("You are out of funds! Try choosing another game!")
                elif user_game_type=="SN":
                    final_user_guess=correct_type_of_guess_roulette()
                    final_user_bet=correct_type_of_bet()
                    if money-35*final_user_bet>=0:
                        money+=roulette(final_user_guess, user_game_type, final_user_bet)
                        print("You now have {0} credits left".format(money))
                    else:
                        print("You are out of funds! Try choosing another game!")
                else:
                    dont_get_back=False
                
        else:
            play_again=False
            print("Thank you for playing our games! Enjoy your {0} credits!".format(money))
            
play_games()
        
    
    
