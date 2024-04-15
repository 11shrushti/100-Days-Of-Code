# Hangman Gamae

import random
word_list = ["valuation" , "ancorage","camel","cilantro"]

# To chosse a word from the list
chosen_word = random.choice(word_list)



# testing the solution
print (f"The solution is {chosen_word}")

# create a blank space as per the chossen word
display = []
word_len=len(chosen_word)
for _ in range(word_len):
   display += "_"
print(display)


# tell the user to guess the letter 
guess = input("Guess the letter: \n").lower()
# this is  to display the letter in the blanks
for posistion in range(word_len):
   letter = chosen_word[posistion]
   if letter == guess:
      display[posistion]=letter
print(display)      


      
    