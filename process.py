import random
import sys

try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a number.")
    sys.exit(1)

text = " ".join(sys.argv[2:])
print("text", text)


def number_puzzle():
    print("<h1>Number Puzzle</h1>")
    answer = (
        "<p>The number "
        + str(number)
        + " is {{even_odd}} and it's {{square_root_cube}}.</p>"
    )
    if number % 2 == 0:
        print(
            answer.replace("{{even_odd}}", "even").replace(
                "{{square_root_cube}}", f"square root is {number**0.5}"
            )
        )
    else:
        print(
            answer.replace("{{even_odd}}", "odd").replace(
                "{{square_root_cube}}", f"cube is {number**3}"
            )
        )


def text_puzzle():
    print("<h1>Text Puzzle</h1>")
    binary = " ".join(format(ord(i), "08b") for i in text)
    print(f"<p>The binary representation of the text is: \n {binary}</p>")
    number_of_vowels = sum(1 for char in text if char in "aeiou")
    print(f"<p>The text contains {number_of_vowels} vowels.</p>")


def initial_message(attempts, num):
    if attempts == 0:
        print("<h2>Guess a number between 1 and 100: </h2>")
    elif attempts >= 5:
        print("<h3>You have reached the maximum number of attempts.</h3>")
        print(f"<h3>The treasure was hidden at {num}.</h3>")
        return True
    else:
        print(f"<h2>Try again. You have {5 - attempts} attempts left.</h2>")


def treasure_hunt():
    print("<h1>Treasure Hunt</h1>")
    guess = 0
    num = random.randint(1, 100)
    attempts = 0
    min_val = 1
    max_val = 100
    guesses = []
    while guess != num:
        end = initial_message(attempts, num)
        if end:
            break
        guess = random.randint(min_val, max_val)
        while guess in guesses:
            guess = random.randint(min_val, max_val)
        guesses.append(guess)
        if guess < num:
            min_val = guess
        else:
            max_val = guess
        print(
            f"<p>{guess} is {num > guess and 'less' or 'greater'} than the treasure.</p>"
        )
        attempts += 1

    if guess == num:
        print(
            f"<h2>Congratulations! You found the treasure in {attempts} attempts.</h2>"
        )


number_puzzle()
text_puzzle()
treasure_hunt()
