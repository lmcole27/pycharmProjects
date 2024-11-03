#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

import random
solution = random.choice(word_list)
print(solution)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input(f"Choose a letter\n")
guess = guess.lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#solution_len = len(solution)
#x = 0

for letter in solution:
  if guess == letter:
    print("Correct")
  else:
    print("Incorrect")
#  x += 1

#for letters in solution_len:
#letters = []
#letters.append(letter)