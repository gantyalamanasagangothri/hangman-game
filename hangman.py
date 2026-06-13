import random

def display_hangman(tries):
    """Display the hangman figure based on remaining tries"""
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def get_word():
    """Return a random word from the predefined list"""
    word_list = ["python", "hangman", "computer", "programming", "keyboard"]
    return random.choice(word_list).upper()


def display_board(word, guessed_letters):
    """Display the current state of the word with guessed letters"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display


def play_hangman():
    """Main game loop"""
    word = get_word()
    guessed_letters = set()
    incorrect_guesses = set()
    tries = 6
    game_over = False
    won = False

    print("\n" + "="*50)
    print("WELCOME TO HANGMAN!")
    print("="*50)
    print(f"\nThe word has {len(word)} letters.")
    print("You have 6 incorrect guesses allowed.\n")

    while not game_over:
        # Display hangman drawing
        print(display_hangman(tries))

        # Display current board state
        print("\nWord: ", display_board(word, guessed_letters))

        # Display guessed letters
        if guessed_letters:
            print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        if incorrect_guesses:
            print("Incorrect guesses:", " ".join(sorted(incorrect_guesses)))
        
        print(f"Remaining incorrect guesses: {tries}")

        # Get player input
        guess = input("\nGuess a letter: ").upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("❌ You already guessed that letter!")
            continue

        # Check if guess is correct
        if guess in word:
            guessed_letters.add(guess)
            print(f"✓ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            tries -= 1
            print(f"✗ Sorry, '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            game_over = True
            won = True

        # Check lose condition
        if tries == 0:
            game_over = True
            won = False

    # Game Over
    print("\n" + "="*50)
    if won:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"The word was: {word}")
    else:
        print(display_hangman(tries))
        print("💀 GAME OVER! YOU LOST! 💀")
        print(f"The word was: {word}")
    print("="*50 + "\n")


def main():
    """Main function to handle game replay"""
    play_again = True
    
    while play_again:
        play_hangman()
        
        response = input("Do you want to play again? (yes/no): ").lower()
        while response not in ["yes", "no", "y", "n"]:
            response = input("Please enter 'yes' or 'no': ").lower()
        
        play_again = response in ["yes", "y"]
    
    print("Thanks for playing Hangman! Goodbye!")


if __name__ == "__main__":
    main()
