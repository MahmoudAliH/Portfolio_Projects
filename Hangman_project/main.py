#Step 1
##Step 2
import random

import hangman_art
import hangman_words

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

##Testing code
print(f"The solution is {chosen_word}.")
#TODO-2 - Ask the user to guess a letter and assigne their answer to a variable called guess. Make guess lowercase.

##Create an empty List called display.
display = []

##For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(len(chosen_word)):
  display += "_"

print(display)
##So if the chose_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

##Loop through each position in the chosen_word;
##If the letter at that position matches 'guess' then reveal that letter in the display at that position.
##e.g If the user guessed "p" and the chosen word was "apple", the display should be ["_", "p", "p", "", "_"].
#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
end_of_game = False
lives = 6
print(lives)
while not end_of_game:
  guess = input("guess a letter: ").lower()
  
  if guess in display:
        print(f"You've already guessed {guess}")

  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if guess == letter:
        display[position] = letter
        #display.insert(position, guess)
  #Join all the elements in the list and turn it into a String.
  print(display)
  #print(f"{' '.join(display)}")
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(hangman_art.stages[lives])
    lives -= 1
    if lives < 0:
      end_of_game = True
      print("You lose.")

  if "_" not in display:
    end_of_game = True
    print("you win")
  
  
## Print 'display and you should see the guessed letter in the correct position and every other letter replace with "_".
##Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.