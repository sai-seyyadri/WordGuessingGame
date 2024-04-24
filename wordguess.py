import random
import letter_count
import os

file = open('word_guessgame_results.txt', 'a')

def word_choice():
    word_bank = ['banana', 'orange','apple', 'strawberry', 'peach','apricot','pomegranate', 'pineapple', 'papaya', 'raspberries','grapes', 'watermelon', 'mango', 'blueberry', 'cherry', 'pear', 'grapefruit']
    word = random.choice(word_bank).lower()
    return word
    
def guess_word(word, word_think):
    guess_word = ""
    for character in word:
        if character in word_think:
            guess_word = guess_word + character
    return guess_word
    
def character_collected(word):
    guess_character = []
    total_chances = 3 
    winner='No one'
    winnerscore=100
    print("Welcome to Word Guessing Game! The theme is Fruits! ")
    print("For more information & instructions please look at README.md") 
    print ("The word you are going to guess is "+ str(len(word)) + " characters long" )
    NumberofPlayers = int(input("Enter number of players to play\n"))
    
    while True:
        if NumberofPlayers !=0:
           
            PlayerName = input("Player Name\n")
            total_chances = 3 
            letterCount=0 
            
            while True:
                if total_chances !=0:
                    print(f"You have {total_chances} chances ")
                    print(" Correct letters guessed till now: " + guess_word(word, guess_character))
                    print(" Letters guessed so far: " + str(guess_character))
                    guessWord = input("Enter a letter or a word to guess: ").lower()
                    guessLetter = guessWord[0]
                    letterCount = letterCount+1
                    
                    if guessWord == word:
                       print("Congrats! You guessed the correct word!")
                       file.write('Congrats!! ' + PlayerName + ' you guessed correct still '+ str(total_chances) +' chances left and score with '+str(letterCount) +'\n')
                       if letterCount < winnerscore:
                           winner=PlayerName
                           winnerscore=letterCount
                       total_chances = 0
                       NumberofPlayers = NumberofPlayers - 1
                       guess_character.clear()
                       break
                    
                    if guessLetter not in guess_character:
                        guess_character.append(guessLetter)
                       
                    if guessLetter in word:
                        print( "'"+guessLetter +"'"+ " is in the word " )
                        char_frequency = letter_count.count_char(word, guessLetter);
                        print("Frequency of letter is: " + str(char_frequency))
                    else:
                        if len(guessWord) ==1:
                            print("'"+guessLetter +"'"+ " is not in the word") 
                        else:
                            print("'"+guessWord +"'"+ " is not the correct word")
                    if len(guessWord) > 1:
                        total_chances = total_chances - 1
                else:
                    NumberofPlayers = NumberofPlayers - 1
                    guess_character.clear()
                    file.write('Sorry ' + PlayerName + ' you guessed wrong still '+ str(total_chances) +' chances left and score with '+str(letterCount) +'\n')
                    break
            print("End of game for, ", PlayerName)
            print("Number of players remaining ", NumberofPlayers) 
        else:
            print(f"End of Game, Final Winner is ", winner) 
            file.write(f"End of Game, Final Winner is, " + winner +'\n')  
            file.write('**************************************************************************************'+'\n')            
            break        
while True:
    word = word_choice()
    character_collected(word)
    if input("Do you want to continue (y/n): ").lower().startswith("n"):
       break