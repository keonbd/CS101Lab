print('Welcome to the Flarsheim Guesser!')

def game():   #this will define the game into a function, so it can play again'''
    division_3 = -1   #these are set to -1 so they can be used in the while loops later on in the code'''
    division_5 = -1
    division_7 = -1
    number = int(input('Please think of a number between and including 1 and 100.'))

    while division_3 < 0 or division_3 > 2:       #This will keep the loop running until the user enters a valid variable'''
        division_3 = int(input('What is the remainder when your number is divided by 3 ?'))
        if division_3 < 0:
            print('The number you enter needs to be 0 or greater')
        if division_3 > 2:
            print('The number you enter needs to be less that 3')

    while division_5 < 0 or division_5 > 4:       #This will keep the loop running until a valid vairable is entered'''
        division_5 = int(input('What is the remainder when your number is divided by 5 ?'))
        if division_5 < 0:
            print('The number you enter needs to be 0 or greater')
        if division_5 > 4:
            print('The number you enter needs to be less that 5')

    while division_7 < 0 or division_7 > 6:       #This will keep the loop running until a valid variable is entered'''
        division_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        if division_3 < 0:
            print('The number you enter needs to be 0 or greater')
        if division_3 > 2:
            print('The number you enter needs to be less that 3')

    for i in range(0,100+1):
        if i % 3 == division_3 and i % 5 == division_5 and i % 7 == division_7:
            print(f'The number you chose was ', {i})    #this compares all three numbers remainders and find a number through the range that will fit into all three of the users remainder inputs'''

    play = input('Do you want to to play again')
    if play == 'Y':   #This will continue the game if the player enters Y'''
        game()
    elif play == 'N':    #This will quit the game'''
        quit
    while play != 'Y' and play != 'N':    #This will continue to ask the player if they want to play until they enter a valid response to either quit or play'''
        play = input('Do you want to play again')

game()
