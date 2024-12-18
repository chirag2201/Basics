import random
def number_guesing_game():
    print("Welcome to number guessing game.")
    print("I'm thinking of number between 1 to 10.")
    print("You've 10 attempts to guess it. \n")

    #generate a random number
    secret_number = random.randint(1,10)

    #Number of attempts
    attempts = 3

    while attempts > 0:
        try:
            #take user input
            guess = int(input("Enter your guess: "))

            #Validate guess
            if guess < 1 or guess > 10:
                print("Please enter a number betwenn 1 to 10")
                continue

            #check the guess
            if guess == secret_number:
                print(f"Congratulations you guessed the right!. The number was {secret_number}.")
                break
            elif guess < secret_number:
                print("Too Low!. Try again")
            else:
                print("Too high!. Try again")

            #Decrease attempts 
            attempts -= 1
        
        except ValueError:
            print(f"{guess} is an Invalid input! Please enter a valid number.")

    if attempts == 0:
        print(f"Sorry you're out of attempts. The number was {secret_number}. Better luck next time!")

if __name__ == "__main__":
    number_guesing_game()
