import random

# List of 5-letter words (sample, you can expand this)
WORDS = ["apple", "grape", "peach", "mango", "lemon", "berry", "melon", "plums"]

def pick_word():
    return random.choice(WORDS)

def get_feedback(guess, answer):
    result = []
    answer_chars = list(answer)
    # First pass: Green (correct letter, correct position)
    for i, c in enumerate(guess):
        if c == answer[i]:
            result.append("🟩")
            answer_chars[i] = None
        else:
            result.append(None)
    # Second pass: Yellow (correct letter, wrong position), or Gray
    for i, c in enumerate(guess):
        if result[i] is None:
            if c in answer_chars:
                result[i] = "🟨"
                answer_chars[answer_chars.index(c)] = None
            else:
                result[i] = "⬜️"
    return "".join(result)

def main():
    answer = pick_word()
    attempts = 6
    print("Welcome to Wordle!")
    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{attempts}: ").lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print("Please enter a valid 5-letter word.")
        feedback = get_feedback(guess, answer)
        print(f"Feedback: {feedback}")
        if guess == answer:
            print(f"Congratulations! You guessed the word '{answer}' in {attempt} tries.")
            return
    print(f"Sorry! The word was '{answer}'.")

if __name__ == "__main__":
    main()
