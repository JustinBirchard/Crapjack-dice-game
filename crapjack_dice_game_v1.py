# crapjack_dice_game_v1.py
"""A two player dice game similar to Black Jack."""

# imports random module into script so that randrange function can be used
import random

# custom function that rolls two 6 sided "dice" and stores the results as a tuple
def roll_dice ():
    """Roll four dice and return their face values as a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)

# custom function that displays results from dice_roll function
def display_dice(dice):
    """Display the face values of the dice that were rolled in roll_dice function"""
    die1, die2 = dice
    print (f'You rolled {die1} + {die2} = {sum(dice)}')

# Intro message to players and option to see game rules
print('\nWelcome to Crapjack. The first in a series of crappy games.\n')

# power_switch set for 'Booting' conditions
power_switch = 'Booting'

# At this point players can request to view game rules
rules_request = input("For game rules enter 'r'. Otherwise hit enter to start: ")

while power_switch == 'Booting':
    if rules_request == 'r':
        print('\nCrapjack is a two player dice game similar to Blackjack except not as fun.\n'
'\nTo win a match you must score higher than the other player without exceeding 24 points.\n'
'\nA game consists of as many matches as the players wish.\n'
'\nWhoever wins the most matches wins the game.\n'
"\nOn your turn you will roll two dice. The sum of the two dice is your roll's point value."
'\nEach round, you can choose whether to keep or discard your first roll. If you keep it, the point'
'\nvalue will be added to your score. Otherwise you can discard and roll again.' 
'\n\nYou may only discard once per round. After discarding, your next roll will automatically be assigned' 
'\nto your score.'
'\n\nWhen you are done rolling, you must decide whether to finalize your score. If you finalize, it means'
'\nthat you are committing to your score and declining to take anymore turns during the current match.' 
'\nIf you decline to finalize, you will be in line to take another turn on the next round.'
'\n\nAfter player 1 completes their turn, player 2 repeats the same process.\n'
'\nThe round is complete once both players have decided whether or not to finalize their scores.'
'\n\nThe match continues until both players have finalized their scores, or until one player goes over 24 points.'
'\n\nIf either of the players goes above 24 points during a round, the match will automatically end.'
'\n\nIn order to prevent you from harming yourself, if you score exactly 23 or 24 points your score will'
'\nautomatically be finalized.'
'\n\nIf players finalize with identical scores, the match will restart and the player scores will be reset.\n\n'
"At the end of each match players are asked whether they'd like to continue. Choosing to continue will start\n"
'a new match. Declining to continue will end the game and a grand champion will be declared.\n')

        rules_request = 'null'
        input('Press enter to approach the ARENA OF CHAMPIONS: ')

# Once players exit the game rules section, the power_switch transitions to 'Standby' while player names are entered
    else:
        power_switch = 'Standby'

        p1_name = input('Player 1 name: ')
        p2_name = input('Player 2 name: ')

        while power_switch == 'Standby':
# power_switch will remain in 'Standby' until players enter at least one character as their name
            if p1_name == '':
                p1_name = input("Player 1, try again. Your name can be dumb, but it can't be blank: ")
            
            elif p2_name == '':
                p2_name = input("Player 2, try again. Your name can be ridiculous but it can't be nonexistent: ")
# After entering player names, the power_switch is flipped to 'On' triggering the MAIN LOOP
            else:
                power_switch = 'On'
                print('')
#New game scenario will be triggered by game_status update
                game_status = 'New Game'

# MAIN LOOP begins:
        while power_switch == 'On':

# Below is where the variables and trackers are set for all possible game scenarios 
# Depending on the current scenario, players are either sent to the HEART OF THE GAME LOOP
# or given the option to quit and exit the program.

# Varibables callibrated if 'New Game' scenario is triggered
            if game_status == 'New Game':
                p1_score = 0
                p2_score = 0
                p1_match_wins = 0
                p2_match_wins = 0
                p1_status = 'Active'
                p2_status = 'Active'
                game_status = 'Continue'
                round = 1
                extra_rounds = 0
                total_rounds = 0
                match = 1

# Variables callibrated if 'Match Tie' scenario is triggered
            elif game_status == 'Match Tie':
                p1_score = 0
                p2_score = 0
                p1_status = 'Active'
                p2_status = 'Active'
                game_status = 'Continue'
                round = 1
                round += extra_rounds

# Variables callibrated if 'New Match' scenario is triggered
            elif game_status == 'New Match':
                p1_score = 0
                p2_score = 0
                p1_status = 'Active'
                p2_status = 'Active'
                game_status = 'Continue'
                round = 1
                match += 1

# Option to start new match or quit if 'Match Over' scenario is triggered
            elif game_status == 'Match Over':
                game_restart = input('\nWould you like to play again? (y/n): ')
                if p1_status == 'Finalized' and game_restart == 'y':
                    total_rounds += round
                    game_status = 'New Match'
                    input('Hit enter to begin new match: ')
# If players decline to play another match the game winner is displayed and the program shuts down.
                elif p1_status == 'Finalized' and game_restart == 'n':
                    total_rounds += round
                    print(f'\nGame over. You played {match} matches and {total_rounds} total rounds.\n')
                    print(f'{p1_name} total match wins: {p1_match_wins}')
                    print(f'{p2_name} total match wins: {p2_match_wins}')

                    if p1_match_wins > p2_match_wins:
                        print(f'\n{p1_name} is the GRAND CHAMPION!')
                        print('\nThanks for playing!')
                        input('Hit enter to step away from the ARENA OF CHAMPIONS and close the program: ')						
                        break

                    elif p2_match_wins > p1_match_wins:
                        print(f'\n{p2_name} is the GRAND CHAMPION!')
                        print('\nThanks for playing!')
                        input('Hit enter to step away from the ARENA OF CHAMPIONS and close the program: ')						
                        break

                    else:
                        print("\nLooks like you decided to end the game while tied. \n\nWell isn't that nice.")
                        print('\nDue to your lack of courage, there will be no grand champion declared today.')
                        print('\nThanks for playing... I guess.\n')
                        input('Hit enter to cowardly slink away from the ARENA OF CHAMPIONS and close the program: ')
                        break
# If 'y' or 'n' are not chosen the 'restart Error' loop will begin
                else:
                    p1_status = 'restart Error'
                    game_restart = input("You must choose either 'y' or 'n': ")

                    if game_restart == 'y':
                        total_rounds += round
                        game_status = 'New Match'
                        input('Hit enter to begin new match: ')

                    elif game_restart == 'n':
                        total_rounds += round
                        print(f'\nGame over. You played {match} matches and {total_rounds} total rounds.\n')
                        print(f'{p1_name} match wins: {p1_match_wins}')
                        print(f'{p2_name} match wins: {p2_match_wins}')

                        if p1_match_wins > p2_match_wins:
                            print(f'\n{p1_name} is the GRAND CHAMPION!')
                            print('\nThanks for playing!')                    
                            break

                        elif p2_match_wins > p1_match_wins:
                            print(f'\n{p2_name} is the GRAND CHAMPION!')
                            print('\nThanks for playing!\n')                    
                            break

                        else:
                            print("\nLooks like you decided to end the game while tied. \n\nWell isn't that nice.")
                            print('\nDue to your lack of courage, there will be no grand champion declared today.')
                            print('\nThanks for playing... I guess.\n')
                            input('Hit enter to cowardly slink away from the ARENA OF CHAMPIONS and close the program: ')
                            break

# Below is the HEART OF THE GAME LOOP
# Players roll "dice" and make decisions until end-game scenario is reached

# Player 1 turn begins
            elif game_status == 'Continue':
                if p1_status == 'Active':
                    input(f'{p1_name} hit enter to roll dice: ')
                    p1_die_values = roll_dice ()
                    display_dice(p1_die_values)
                    p1_decision = input('Keep or Discard? (k/d): ')

                    if p1_decision == 'k':
                        p1_score += (sum(p1_die_values))            
                        print(f'Your score is {p1_score}')

                        if p1_score == 23 or p1_score == 24:
                            p1_status = 'Finalized'
                            print(f'Your score of {p1_score} has been finalized\n')
            
                        elif p1_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.\n')

                        else:
                            p1_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p1_final_decision == 'y':
                                p1_status = 'Finalized'
                                print('')

                            elif p1_final_decision == 'n':
                                p1_status = 'Waiting'
                                print('') 

                            else:
                                p1_status = 'final Error'

                    elif p1_decision == 'd':
                        input(f'{p1_name} hit enter to roll dice: ')
                        p1_die_values = roll_dice ()
                        display_dice(p1_die_values)
                        p1_score += (sum(p1_die_values))
                        p1_status = 'Waiting'
                        print(f'Your score is {p1_score}')
            
                        if p1_score == 23 or p1_score == 24:
                            p1_status = 'Finalized'
                            print(f'Your score of {p1_score} has been finalized')
            
                        elif p1_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.')

                        else:
                            p1_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p1_final_decision == 'y':
                                p1_status = 'Finalized'
                                print('')

                            elif p1_final_decision == 'n':
                                p1_status = 'Waiting'
                                print('')
                
                            else:
                                p1_status = 'final Error'

                    else:
                        p1_status = 'kd Error'
# If Player 1 doesn't choose 'k' or 'd', the 'kd Error' loop will begin
                elif p1_status == 'kd Error':
                    p1_decision = input("You must choose either 'k' or 'd': ")

                    if p1_decision == 'k':
                        p1_score += (sum(p1_die_values))            
                        print(f'Your score is {p1_score}')

                        if p1_score == 23 or p1_score == 24:
                            p1_status = 'Finalized'
                            print(f'Your score of {p1_score} has been finalized\n')
            
                        elif p1_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.\n')

                        else:
                            p1_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p1_final_decision == 'y':
                                p1_status = 'Finalized'
                                print('')

                            elif p1_final_decision == 'n':
                                p1_status = 'Waiting'
                                print('') 

                            else:
                                p1_status = 'final Error'

                    elif p1_decision == 'd':
                        input(f'{p1_name} hit enter to roll dice: ')
                        p1_die_values = roll_dice ()
                        display_dice(p1_die_values)
                        p1_score += (sum(p1_die_values))
                        p1_status = 'Waiting'
                        print(f'Your score is {p1_score}')
            
                        if p1_score == 23 or p1_score == 24:
                            p1_status = 'Finalized'
                            print(f'Your score of {p1_score} has been finalized')
            
                        elif p1_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.')

                        else:
                            p1_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p1_final_decision == 'y':
                                p1_status = 'Finalized'
                                print('')

                            elif p1_final_decision == 'n':
                                p1_status = 'Waiting'
                                print('')

                            else:
                                p1_status = 'final Error'

                    else:
                        p1_status = 'kd Error'
# If Player 1 doesn't choose 'y' or 'n' when asked to finalize, the 'final Error' loop will begin
                elif p1_status == 'final Error':
                    p1_final_decision = input("You must choose either 'y' or 'n': ")

                    if p1_final_decision == 'y':
                        p1_status = 'Finalized'
                        print('')

                    elif p1_final_decision == 'n':
                        p1_status = 'Waiting'
                        print('')
        
                    else:
                        p1_status = 'final Error'
# Player 2 turn begins
                elif (p1_status == ('Waiting') or p1_status == ('Finalized')) and p2_status == ('Active'):
                    input(f'{p2_name} hit enter to roll dice: ')
                    p2_die_values = roll_dice ()
                    display_dice(p2_die_values)
                    p2_decision = input('Keep or Discard? (k/d): ')

                    if p2_decision == 'k':
                        p2_score += (sum(p2_die_values))
                        p2_status = 'Waiting'
                        print(f'Your score is {p2_score}') 

                        if p2_score == 23 or p2_score == 24:
                            p2_status = 'Finalized'
                            print(f'Your score of {p2_score} has been finalized\n')
            
                        elif p2_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.\n')

                        else:
                            p2_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p2_final_decision == 'y':
                                p2_status = 'Finalized'
                                print('')

                            elif p2_final_decision == 'n':
                                p2_status = 'Waiting'
                                print('')

                            else:
                                p2_status = 'final Error'

                    elif p2_decision == 'd':
                        print(p2_name, 'hit enter to roll dice')
                        input('')
                        p2_die_values = roll_dice ()
                        display_dice(p2_die_values)
                        p2_score += (sum(p2_die_values))
                        p2_status = 'Waiting'
                        print(f'Your score is {p2_score}')
            
                        if p2_score == 23 or p2_score == 24:
                            p2_status = 'Finalized'
                            print(f'Your score of {p2_score} has been finalized')
            
                        elif p2_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.\n')

                        else:
                            p2_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p2_final_decision == 'y':
                                p2_status = 'Finalized'
                                print('')

                            elif p2_final_decision == 'n':
                                p2_status = 'Waiting'
                                print('')

                            else:
                                p2_status = 'final Error'
# If Player 2 doesn't choose 'k' or 'd', the 'kd Error' loop will begin
                    else:
                        p2_status = 'kd Error'

                elif p2_status == 'kd Error':
                    p2_decision = input("You must choose either 'k' or 'd': ")

                    if p2_decision == 'k':
                        p2_score += (sum(p2_die_values))            
                        print(f'Your score is {p2_score}')

                        if p2_score == 23 or p2_score == 24:
                            p2_status = 'Finalized'
                            print(f'Your score of {p2_score} has been finalized\n')
            
                        elif p2_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.\n')

                        else:
                            p2_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p2_final_decision == 'y':
                                p2_status = 'Finalized'
                                print('')

                            elif p2_final_decision == 'n':
                                p2_status = 'Waiting'
                                print('') 

                            else:
                                p2_status = 'final Error'

                    elif p2_decision == 'd':
                        input(f'{p2_name} hit enter to roll dice: ')
                        p2_die_values = roll_dice ()
                        display_dice(p2_die_values)
                        p2_score += (sum(p2_die_values))
                        p2_status = 'Waiting'
                        print(f'Your score is {p2_score}')
            
                        if p2_score == 23 or p2_score == 24:
                            p2_status = 'Finalized'
                            print(f'Your score of {p2_score} has been finalized')
            
                        elif p2_score > 24:
                            p1_status = 'Finalized'
                            p2_status = 'Finalized'
                            print('Uh oh, your score is higher than 24.')

                        else:
                            p2_final_decision = input('Would you like to finalize? (y/n): ')
            
                            if p2_final_decision == 'y':
                                p2_status = 'Finalized'
                                print('')

                            elif p2_final_decision == 'n':
                                p2_status = 'Waiting'
                                print('')

                            else:
                                p2_status = 'final Error'

                    else:
                        p2_status = 'kd Error'
# If Player 2 doesn't choose 'y' or 'n' when asked to finalize, the 'final Error' loop will begin
                elif p2_status == 'final Error':
                    p2_final_decision = input("You must choose either 'y' or 'n': ")

                    if p2_final_decision == 'y':
                        p2_status = 'Finalized'
                        print('')

                    elif p2_final_decision == 'n':
                        p2_status = 'Waiting'
                        print('')
        
                    else:
                        p2_status = 'final Error'

# When game reaches this condition the round is over 
# Game trackers are adjusted and HEART OF THE GAME LOOP restarts
                elif p1_status == 'Waiting' and p2_status == 'Waiting':
                    p1_status = 'Active'
                    p2_status = 'Active'
                    round += 1
                    extra_rounds = 0
                    print(f'Round {round - 1} is complete. Hit enter to start round {round}.')
                    input('')
                    print(f"{p1_name}'s score is {p1_score}")
                    print(f"{p2_name}'s score is {p2_score}\n")

# If one player has finalized and the other has not,
# the following two elif's will restart the HEART OF THE GAME LOOP for the appropriate player
                elif p1_status == 'Finalized' and p2_status == 'Waiting':
                    p2_status = 'Active'
                    round += 1
                    print(f'Round {round - 1} is complete. Hit enter to start round {round}.')
                    input('')
                    print(f"{p1_name} has finalized with a score of {p1_score}")
                    print(f"{p2_name}'s score is {p2_score}\n")

                elif p1_status == 'Waiting' and p2_status == 'Finalized':
                    p1_status = 'Active'
                    round += 1
                    print(f'Round {round - 1} is complete. Hit enter to start round {round}.')
                    input('')
                    print(f"{p2_name} has finalized with a score of {p2_score}")
                    print(f"{p1_name}'s score is {p1_score}\n")

# If players tie, their scores will be reset and the 'Match Tie' scenario will trigger from the MAIN LOOP
                elif p1_status == ('Finalized') and p2_status == ('Finalized') and p2_score == p1_score:
                    input(f'Holy son of a bun, you tied at {p1_score}! Hit enter to play on and break the tie.: ')
                    game_status = 'Match Tie'
                    extra_rounds = round

# If match-ending conditions are met, the 'Match Over' scenario will trigger from the MAIN LOOP
# Players will receive match summary and scores	
                elif p1_status == 'Finalized' and p2_status == 'Finalized':
                    game_status = 'Match Over'
                    print(f'Match over. You battled valiantly for {round} rounds.\n Hit Enter.')
                    input('')

                    if  p1_score > 24:
                        print(f'{p1_name} scored above the limit with {p1_score}')
                        print(f'{p2_name} wins the match with {p2_score}')
                        p2_match_wins += 1

                    elif  p2_score > 24:
                        print(f'{p2_name} scored above the limit with {p2_score}')
                        print(f'{p1_name} wins the match with {p1_score}')
                        p1_match_wins += 1

                    elif  p1_score > p2_score and p1_score <= 24:
                        print(f'{p1_name} beat {p2_name}')
                        print(f'{p1_score} to {p2_score}')
                        p1_match_wins += 1

                    elif p2_score > p1_score and p2_score <= 24:
                        print(f'{p2_name} beat {p1_name}')
                        print(f'{p2_score} to {p1_score}')
                        p2_match_wins += 1

#**************************************************************************
#* Thank you for taking the time to review my code!                       *
#* Mary Broadway and I made up this game on 4/21/20 using real dice.      *
#* The next day I started coding it, and I finished on 4/29/20            *
#* (which happened to be my 39th birthday!)                               *
#*                                                                        *
#* (C) Copyright 2020 Justin Birchard. All Rights Reserved.               *
#*                                                                        *
#* Want to hear a song? Check out my music: 7sidedrecords.com             *
#**************************************************************************