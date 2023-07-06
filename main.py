import random


genres = ['Rock', 'Pop', 'Hip Hop', 'Country', 'Jazz', 'Electronic', 'Classical']


def generate_genre():
    return random.choice(genres)


def check_guess(genre, guess):
    return genre.lower() == guess.lower()


def music_genre_guessing_game():
    genre = generate_genre()
    attempts = 5

    print("Welcome to Hadif Music Genre Guessing Game!!!")
    print("Guesss the right music genre! >;).You have 3 attempts.")

    while attempts > 0:
        print("genres:")
        print(", ".join(genres))   

        user_guess = input("Enter your guess!: ")

        if check_guess(genre, user_guess):
            print("Congratulations! you was right!")
            return

        attempts -= 1
        print("YOU WRONG!!. You only has", attempts, "attempts remaining...")
    
    print("Game Over,loser. The correct genre was:", genre)


music_genre_guessing_game()