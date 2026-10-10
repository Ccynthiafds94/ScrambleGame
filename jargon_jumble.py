# import random

# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# word = random.choice(words)
# print(f"Randomly selected word: {word}")

# letters = list(word)
# random.shuffle(letters)
# print(letters)

# scrambled_word = ''.join(letters)
# print(f"Scrambled word: {scrambled_word}")

# Challenge: Add a Game Loop
# Right now the game ends after a single word. Add the ability to play multiple rounds and quit out of the game at any point.

# 1. Wrap the game code in a loop that runs for 5 rounds. 
# 2. Display the round number at the beginning of each round. 
# 3. Give the player a way to quit early by typing 'quit'.
#    * Hint: you'll want to break out of the loop when they do.

# import random

# words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
# word_bank = [
#     ("apple", "A fruit that is red and round"),
#     ("banana", "A tropical fruit with a yellow peel"),
#     ("cherry", "A small, round fruit that is red"),
#     ("date", "A sweet, brown fruit that grows on trees"),
#     ("elderberry", "A dark purple fruit that grows on shrubs"),
#     ("fig", "A soft, sweet fruit with a unique shape"),
#     ("grape", "A small, round fruit that grows in clusters"),
#     ("honeydew", "A large, green melon with a sweet interior")
# ]

# ROUNDS = 5
# round_no = 1
# score = 0
# used = []

# while round_no <= ROUNDS:
#     print(f"Round {round_no}")
#     print("-" * 20)
#     word, hint = random.choice(word_bank)
    
#     while (word, hint) in used:
#         word, hint = random.choice(word_bank)
    
#     used.append((word, hint))

#     letters = list(word)
#     random.shuffle(letters)
#     scrambled_word = "".join(letters).upper()
#     print(f"Scrambled: {scrambled_word}")
#     print()

#     guess = input("Guess the word (or type 'hint' / 'skip' / 'quit' ): ").strip().lower()

#     if guess == "hint":
#         print()
#         print(f"Hint: {hint}")
#         print()
#         guess = input("Your guess (or 'skip'): ").strip().lower()

#     if guess == "quit":
#         print("Thanks for playing!")
#         break
#     elif guess == "skip":
#         print(f"Skipped! The word was '{word}'.")
#     elif guess == word:
#         print("✅  Correct!")
#         score += 1
#     else:
#         print(f"❌ Sorry, the word was '{word}'.")
        
#     round_no += 1

# print(f"Game Over! Your score: {score}/{ROUNDS}")

# if score == 5:
#   print("Flawless! All tests passing, zero bugs.")
# elif score == 4: 
#   print("Near perfect, only one failing test!")
# elif score == 3:
#   print("Halfway there, three tests passing.")
# else:
#   print("Two tests passing, two failing.")  
  
        
# Game improvized

import random
from llm_helpers import get_llm_response, print_llm_response

ROUNDS = 5
MAX_RETRIES = 3
ATTEMPTS = 3

DIFFICULTY = {
    "easy": "4 to 6 letters, very common",
    "medium": "6 to 8 letters, moderately common",
    "hard": "8 or more letters, less common",
}


def get_new_word(category, difficulty, used):
    """Ask the LLM for a word + hint. Returns (word, hint) or None."""
    avoid = ", ".join(used) if used else "none"
    prompt = (
        f"Give me one word from the category '{category}' for a word-scramble game. "
        f"Difficulty: {DIFFICULTY[difficulty]}. "
        "Also give a short hint that does not contain the word itself. "
        f"Do NOT use any of these words: {avoid}. "
        "Reply in exactly this format and nothing else: WORD|HINT "
        "(WORD is a single lowercase word, letters only)."
    )
    for _ in range(MAX_RETRIES):
        reply = get_llm_response(prompt).strip()
        if "|" not in reply:
            continue
        word, hint = reply.split("|", 1)
        word, hint = word.strip().lower(), hint.strip()
        if word.isalpha() and len(word) >= 4 and word not in used and hint:
            return word, hint
    return None


def choose_category():
    print("\nPick a category, e.g. fruits, animals, countries, movies, programming terms...\n")
    while True:
        category = input("Category: ").strip()[:40]
        if category:
            return category
        print("Please enter a category.")


def choose_difficulty():
    while True:
        level = input("Difficulty (easy / medium / hard): ").strip().lower()
        if level in DIFFICULTY:
            return level
        print("Please type easy, medium or hard.")


def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    while "".join(letters) == word:
        random.shuffle(letters)
    return "".join(letters).upper()


def play_game(category, difficulty):
    score = solved_count = played = streak = best_streak = 0
    used = []
    round_no = 1
    quit_game = False

    while round_no <= ROUNDS and not quit_game:
        print(f"\nRound {round_no} of {ROUNDS}  |  {category} ({difficulty})  |  Score: {score}")
        print("-" * 50)

        result = get_new_word(category, difficulty, used)
        if result is None:
            print("Couldn't get a word for that category. Try a different one.")
            category = choose_category()
            continue

        word, hint = result
        used.append(word)
        print(f"Scrambled: {scramble(word)}\n")

        hint_used = False
        solved = skipped = False
        attempt = 1

        while attempt <= ATTEMPTS:
            guess = input(f"\nAttempt {attempt}/{ATTEMPTS} - guess (or 'hint' / 'skip' / 'quit'): ").strip().lower()

            if guess == "quit":
                quit_game = True
                break
            if guess == "skip":
                skipped = True
                break
            if guess == "hint":
                if hint_used:
                    print(f"(You already used it) Hint: {hint}")
                else:
                    hint_used = True
                    print(f"Hint: {hint}  (-4 points)")
                continue  # hints don't use up an attempt
            if guess == word:
                solved = True
                break

            attempt += 1
            if attempt <= ATTEMPTS:
                print(f"❌ Not quite! It starts with '{word[0].upper()}' and has {len(word)} letters.")

        if quit_game:
            print("Thanks for playing!")
            break

        played += 1
        if solved:
            points = max(1, 10 - 3 * (attempt - 1) - (4 if hint_used else 0))
            streak += 1
            best_streak = max(best_streak, streak)
            bonus = 2 * (streak - 1)
            points += bonus
            score += points
            solved_count += 1
            extra = f" (+{bonus} streak bonus!)" if bonus else ""
            print(f"✅ Correct! +{points} points{extra}")
        else:
            streak = 0
            print(f"The word was '{word}'." if skipped else f"💀 Out of attempts! The word was '{word}'.")

        round_no += 1

    return score, solved_count, played, best_streak


def main():
    print("🔤 Welcome to Jargon Jumble!")
    best_score = 0

    while True:
        category = choose_category()
        difficulty = choose_difficulty()
        score, solved, played, best_streak = play_game(category, difficulty)

        print(f"\nGame Over! Score: {score} | Solved: {solved}/{played} | Best streak: {best_streak}")
        if score > best_score:
            best_score = score
            print("🏆 New best score!")
        else:
            print(f"Best score so far: {best_score}")

        if played > 0:
            print_llm_response(
                f"A player finished a word-scramble game in the category '{category}' "
                f"on {difficulty} difficulty: solved {solved} of {played} words, score {score}, "
                f"best streak {best_streak}. Reply with 2 short, playful sentences of feedback "
                "written in software-testing language (tests passing, bugs, etc.). "
                "No more than 35 words."
            )

        again = input("\nPlay again with a new category? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


main()