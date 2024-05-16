The MIT License was used in this game.

In this game, I did a code review with Ishani Ghosh, where we worked on displaying the results into a bar graph (CSV file).
This README.txt is about the Word Guessing Game developed in python.

The theme I took is fruits.

This game can be played by one or two players. All the words are stored in a word bank from which the players have to guess while taking turns.

The player has the opportunity to guess either by entering a single letter or a word. Each time the player enters the letter it is stored in array and displays the letters guess so far and as well as the correct letters guessed.

At the start of the game the player has a hint about the length of the word, and to input the number of players to play.
A validation check for numeric value is done for the input of number of players. 

The player name is entered first and the game starts, showing the number of chances (3), to begin with. As the player guess a letter, it displays the correct letters guessed till now and the letters guessed so far with number of occurrences.

The number of chances will reduce only if the player enters more than 1 letter, which is then considered as a word.
Each player has 3 chances for word guesses, and an unlimited number of letters. For each letter guess the score increases by 1. (A lower score is better)

When the player enters the letter or word, it will be converted to lower case and compares it with the random choice word from the word bank (all the words in word bank are stored in lower case) and if it matches, the player's turn ends with the first player name stored as the winner name. The  information is stored in a separate word_guessgame_results.txt and word_guessgame.csv file. All the variables will be initialised for the next player and the same continues till the player completes his guesses or the enters the correct guess.

If the number of guesses is less than the previous player's guesses, then the winner name variable changes to the latest player name.
Finally the winner name with the remaining number of tries, number of chances, and score will be stored in the output file: word_guessgame_results.txt and the information will keep appending to the text file.

The word_guessgame.csv data displays a bar graph of the results with the Player Name and number of tries.  