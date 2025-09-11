#huess number game (if,elif,else)
import random
def game():

  keep_going = 'y'

  game_over = False

  x = random.randint(1, 100)

  print(x) # DEBUG

  while keep_going == 'y':

    guess = int(input("Enter integer value [1-100]: "))
    if guess > x:

      print("Too high, try again")

    elif guess < x:

      print("Too low, try again")

    elif guess == x:

      print("Congratulations!")

      game_over = True



    if game_over:

      keep_going = input("Continue? [y/n]: ")

      if keep_going == 'y':

        game_over = False

        x = random.randint(1, 100)

        print(x) # DEBUG
        
      elif keep_going == 'n':

        print("Thanks for playing")

        break

      else:

        print("Error: Invalid input")


game()