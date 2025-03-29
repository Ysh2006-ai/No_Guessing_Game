import random

secret_number = random.randint(1, 100)

# Set the number of attempts
attempts = 5

while attempts > 0:
  
  user_guess = int(input("Guess a number between 1 and 100: "))


  if user_guess == secret_number:
    print("Congratulations! You won!")
    break
  elif user_guess < secret_number:
    print("Too low! Try again.")
  else:
    print("Too high! Try again.")

  # Decrement the number of attempts
  attempts -= 1


if attempts == 0:
  print(f"Sorry, you lost! The secret number was {secret_number}.")
