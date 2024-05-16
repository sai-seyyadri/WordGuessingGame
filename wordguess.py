"""  
This script implements a Word Guessing Game where players try to guess a word from a word bank. 
The game tracks player scores and displays the results in a bar chart. The game allows multiple players to 
participate and records their performance in a CSV file and text file. 
"""

import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import letter_count

"""  
Libraries used:
os: Provides operating system functionality
random: Generates random numbers for word selection.
pandas (as pd): Handles data sets and reading/writing the CSV file
matplotlib.pyplot (as plt): Generates bar graph for visualizing game results.
letter_count: Custom module to count character occurrences in a word.
"""  

results_file = 'word_guessgame_results.csv'
Outputfile = open('word_guessgame_results.txt', 'a')

def write_to_csv(player_name, remaining_chances, NumberofTries):
    with open(results_file, 'a') as file:
        file.write(f'{player_name},{remaining_chances},{NumberofTries}\n')
""" 
 write_to_csv(player_name, remaining_chances, NumberofTries): Writes player data to a CSV file.
    Inputs:
        - player_name (str): Name of the player
        - remaining_chances (int): Remaining chances for the player
        - NumberofTries (int): Number of tries made by the player
""" 

def display_results():
    results_df = pd.read_csv(results_file, header=None, names=['Player Name', 'Remaining Chances', 'NumberofTries'])
    print(results_df)
    return results_df
""" 
Displays game results from the CSV file.
Returns: pandas.DataFrame: DataFrame containing game results.
""" 

def guess_word(word, word_think):
    guess_word = ""
    #Empty string to store guessed characters  
    for character in word:
        #Iterate over each character in the word
        if character in word_think:
            #Checks if character is also in word_think (user input)
            guess_word += character
    return guess_word
""" 
Returns a string containing correctly guessed characters of the word.
    Parameters:
     - word (str): The word to be guessed.
     - word_think (list): characters guessed by the player (user input)
    Returns:
    - str: The guessed characters of the word.
""" 
# ---------Tests------------
# guess_word("meth", "something")
# guess_word("somet", "something")
# guess_word("somehingt", "temos")

#Guessed letter: "p"
#Message:'p' is not in the word
#You have 3 chances
#Correct letters guessed till now: 
#Letters guessed so far: ['p']

# Enter a letter or a word to guess: a
#'a' is in the word
#Frequency of letter is: 1
#You have 3 chances
#Correct letters guessed till now: a
#Letters guessed so far: ['p', 'a']
#Enter a letter or a word to guess:

#Enter a letter or a word to guess: strawberry
#'strawberry' is not the correct word
#You have 2 chances
#Correct letters guessed till now: a
#Letters guessed so far: ['p', 'a', 's']

#Enter a letter or a word to guess: mango
#Congrats! You guessed the correct word!
#End of game for Sai
#Number of players remaining 0
#End of Game, Final winner is  Sai
#Do you want to continue (y/n):


def word_choice():
    word_bank = ['banana', 'orange', 'apple', 'strawberry', 'peach', 'apricot', 'pomegranate', 'pineapple', 'papaya', 'raspberries', 'grapes', 'watermelon', 'mango', 'blueberry', 'cherry', 'pear', 'grapefruit']
    word = random.choice(word_bank).lower()
    return word
""" 
Randomly selects a word from a predefined word bank.
""" 
def character_collected(word):
    guess_character = []
    # List to store guessed characters
    total_chances = 3
    # Total chances each player has
    winner = 'no one'
    # Initialize the winner as 'no one'
    winnerscore = 100
    # Initialize the winner's score as a large number
    print("Welcome!! to Word Guessing Game")
    print("For more information & instructions please look at README.md")
    print("The word you are going to guess is " + str(len(word)) + " characters long")
    try:
        NumberofPlayers = int(input("Enter number of players to play\n"))
    except Exception:
        print("Hey, please enter numbers only")
        # ---------------Test------------
        #Enter number of players to play
        #'a' 
        #Message: Hey, please enter numbers only
        #Do you want to continue (y/n):
    else:
        while True:
            if NumberofPlayers != 0:
                PlayerName = input("Player Name\n")
                total_chances = 3
                #Total chances for each player
                letterCount = 0

                while True:
                    if total_chances != 0:
                        # Display remaining chances and guessed characters
                        print(f"You have {total_chances} chances")
                        print("Correct letters guessed till now: " + guess_word(word, guess_character))
                        print("Letters guessed so far: " + str(guess_character))
                        guessWord = input("Enter a letter or a word to guess: ").lower()
                        guessLetter = guessWord[0]
                        # Displays user input 
                        letterCount += 1

                        if guessWord == word:
                            # If the guess matches the word, the player is declared as winner
                            print("Congrats! You guessed the correct word!")
                            write_to_csv(PlayerName, total_chances, letterCount)
                            # Write player info to CSV
                            Outputfile.write('Congrats!! ' + PlayerName + ' you guessed correct still '+ str(total_chances) +' chances left and NumberofTries with '+str(letterCount) +'\n')
                            # Update winner if the current player has a lower score
                            if letterCount < winnerscore:
                                winner = PlayerName
                                winnerscore = letterCount
                            total_chances = 0
                            # Set chances to 0 to end game for this player
                            NumberofPlayers -= 1
                            # Decrement number of players
                            guess_character.clear()
                            # Clear guessed characters for the next player
                            break

                        if guessLetter not in guess_character:
                            guess_character.append(guessLetter)
                            # Add the guessed letter to the list of guessed characters

                        if guessLetter in word:
                            # Feedback for correct guess
                            print("'" + guessLetter + "'" + " is in the word")
                            char_frequency = letter_count.count_char(word, guessLetter)
                            print("Frequency of letter is: " + str(char_frequency))
                            # Count frequency of guessed letter in the word
                        else:
                            # Feedback for incorrect guess
                            if len(guessWord) == 1:
                                print("'" + guessLetter + "'" + " is not in the word")
                            else:
                                print("'" + guessWord + "'" + " is not the correct word")
                        if len(guessWord) > 1:
                            total_chances -= 1
                            # Decrement chances if a word is guessed instead of a letter
                    else:
                        # If player has used up all chances, end game for this player
                        NumberofPlayers -= 1
                        guess_character.clear()
                        Outputfile.write('Sorry ' + PlayerName + ' you guessed wrong still '+ str(total_chances) +' chances left and NumberofTries with '+str(letterCount) +'\n')
                        break
                print("End of game for", PlayerName)
                print("Number of players remaining", NumberofPlayers)
            else:
                print(f"End of Game, Final winner is ", winner)
                Outputfile.write(f"End of Game, Final winner is, " + winner +'\n')  
                Outputfile.write('**************************************************************************************'+'\n')    
                break
""" 
The function initializes a game session with a given word from the word bank. It prompts players to guess characters or the entire word
within a limited number of chances (3). The number of chances is decreased by 1 when a word is guessed, but the player has
unlimited chances to guess characters. After each guess, it provides feedback on correct and incorrect guesses, and tracks 
player scores. The game ends when either all players have exhausted their chances or the word is correctly guessed.
""" 

while True:
    word = word_choice()
    character_collected(word)
    if input("Do you want to continue (y/n): ").lower().startswith("n"):
        break
    # Ask the user if they want to continue playing
    # If the user inputs 'n' or anything starting with 'n', exit the loop and end the game


# Display the results
results_df = display_results()
plt.figure(figsize=(10, 6))
# Set the figure size for the plot
plt.bar(results_df['Player Name'], results_df['NumberofTries'], color='skyblue')
# Bar graph with player names and their number of tries
plt.xlabel('Player Name')
plt.ylabel('NumberofTries')
plt.title('Number of tries by Each Player')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()