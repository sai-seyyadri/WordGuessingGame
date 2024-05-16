The MIT License was used in this game.
This README.txt is about the Word Guessing Game developed in python.

The theme I took is fruits.

This game can be played by more than one player. All the words are stored in word bank from which the players have to guess while taking turns.

The player has the oppurtunity to guess either by entering a single letter or a word, each time the player enters the letter it is stored in array and displays the letters guess so far and as well as the correct letters guessed.

At the start of the game the player has a hint about the lenght of the word, and to input the number of players to play.
A validation check for numeric value is done for the input of number of players. 

Player name to be entered first and the game starts, showing number of chances which is 3 to begin with and as the player guess a letter, it displays the correct letters guessed till now and the letters guessed so far with number of occurencies.

The number of chances will reduce only if the player enters more than 1 letter which is considered as a word.
Each player has 3 chances for word guesses, and unlimited number of letters for each letter the score increases by 1.

when the player enters the letter or word it will be converted to lower case and compares it with the random choice word from the word bank (all the words in word bank are stored in lower case) and if matches the player turn ends with the first player name is stored as the winner name, and there by all the information is stored in separate word_guessgame_results.txt and word_guessgame.csv file, while all the variables will be initialised for the next player and the same continues till the player completes his guesses or the enters the correct guess.

If the number of guess is less the previous player guesses than the winner name variable changes to the latest player name
finally the winner name with the remaining number of chances and score will be stored in the output file and the information of will be keep appending to the text file.

Using word_guessgame.csv data a graphical representation of the results is shown as a bar graph.