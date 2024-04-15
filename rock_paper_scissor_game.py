# this is a rock paper scissor games

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random 

# user input 
image_option = [rock,paper,scissor]
user_input = int(input("Type 0 for rock , 1 for the paper and 2 for the scissor\n "))
print(image_option[user_input])

#computer choice
print("Computers choice")
computer_choice = random.randint(0,2)
print(image_option[computer_choice])

# conditions
if user_input>=3 or user_input<0:
    print("You have invalif number , try again You lose!")

elif user_input > computer_choice:
    print("You win!")
elif user_input==rock and computer_choice==scissor:
    print("You win!")    
elif computer_choice > user_input:
    print("You lose!") 
elif user_input==computer_choice:
    print("Its a draw")      