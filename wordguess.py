import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import letter_count

results_file = 'word_guessgame_results.csv'
Outputfile = open('word_guessgame_results.txt', 'a')

def write_to_csv(player_name, remaining_chances, NumberofTries):
    with open(results_file, 'a') as file:
        file.write(f'{player_name},{remaining_chances},{NumberofTries}\n')


def display_results():
    # Read the results file into a DataFrame
    results_df = pd.read_csv(results_file, header=None, names=['Player Name', 'Remaining Chances', 'NumberofTries'])
    print(results_df)
    return results_df

def guess_word(word, word_think):
    guess_word = ""
    for character in word:
        if character in word_think:
            guess_word += character
    return guess_word

def word_choice():
    word_bank = ['banana', 'orange', 'apple', 'strawberry', 'peach', 'apricot', 'pomegranate', 'pineapple', 'papaya', 'raspberries', 'grapes', 'watermelon', 'mango', 'blueberry', 'cherry', 'pear', 'grapefruit']
    word = random.choice(word_bank).lower()
    return word

def character_collected(word):
    guess_character = []
    total_chances = 3
    winner = 'no one'
    winnerscore = 100
    print("Welcome!! to Word Guessing Game")
    print("For more information & instructions please look at README.md")
    print("The word you are going to guess is " + str(len(word)) + " characters long")
    try:
        NumberofPlayers = int(input("Enter number of players to play\n"))
    except Exception:
        print("Hey, please enter numbers only")
    else:
        while True:
            if NumberofPlayers != 0:
                PlayerName = input("Player Name\n")
                total_chances = 3
                letterCount = 0

                while True:
                    if total_chances != 0:
                        print(f"You have {total_chances} chances")
                        print("Correct letters guessed till now: " + guess_word(word, guess_character))
                        print("Letters guessed so far: " + str(guess_character))
                        guessWord = input("Enter a letter or a word to guess: ").lower()
                        guessLetter = guessWord[0]
                        letterCount += 1

                        if guessWord == word:
                            print("Congrats! You guessed the correct word!")
                            write_to_csv(PlayerName, total_chances, letterCount)
                            Outputfile.write('Congrats!! ' + PlayerName + ' you guessed correct still '+ str(total_chances) +' chances left and NumberofTries with '+str(letterCount) +'\n')
                            if letterCount < winnerscore:
                                winner = PlayerName
                                winnerscore = letterCount
                            total_chances = 0
                            NumberofPlayers -= 1
                            guess_character.clear()
                            break

                        if guessLetter not in guess_character:
                            guess_character.append(guessLetter)

                        if guessLetter in word:
                            print("'" + guessLetter + "'" + " is in the word")
                            char_frequency = letter_count.count_char(word, guessLetter)
                            print("Frequency of letter is: " + str(char_frequency))
                        else:
                            if len(guessWord) == 1:
                                print("'" + guessLetter + "'" + " is not in the word")
                            else:
                                print("'" + guessWord + "'" + " is not the correct word")
                        if len(guessWord) > 1:
                            total_chances -= 1
                    else:
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
while True:
    word = word_choice()
    character_collected(word)
    if input("Do you want to continue (y/n): ").lower().startswith("n"):
        break

# to display the results
results_df = display_results()
plt.figure(figsize=(10, 6))
plt.bar(results_df['Player Name'], results_df['NumberofTries'], color='skyblue')
plt.xlabel('Player Name')
plt.ylabel('NumberofTries')
plt.title('Number of tries by Each Player')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()