import random

secret_number = random.randint(1, 50)

attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input("Guess what the number is between 1 and 50: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Have another guess")
    elif guess > secret_number:
        print("Too high! Have another go")
    else:
        print(f"That's right! You had {attempts} attempts.")
        break

    attempts_left = max_attempts - attempts
    print(f"You have {attempts_left} attempts left.")

if attempts == max_attempts and guess != secret_number:
    print(f"Game over! The right number is {secret_number}.")

