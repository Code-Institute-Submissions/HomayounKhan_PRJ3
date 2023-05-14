import random

# generate a random number between 1 and 10
number = random.randint(1, 10)

# greet the user and ask for their name
print("Hi there! What's your name?")
name = input()

# explain the rules
print(f"Hi {name}, I'm thinking of a number between 1 and 10. Can you guess what it is?")

# give the user 3 chances to guess
for guesses_taken in range(1, 4):
    print("Take a guess:")
    guess = int(input())

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        break # the user guessed the correct number

# display the result
if guess == number:
    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses.")
else:
    print(f"Sorry, {name}. The number I was thinking of was {number}.")
