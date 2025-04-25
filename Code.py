def count_words(text):
    """
    This function takes a string as input and returns the number of words.
    It splits the text using whitespace as the delimiter.
    """
    words = text.strip().split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    print("-------------------------------------")
    
    # Get user input
    user_input = input("Please enter a sentence or paragraph:\n").strip()

    # Error handling for empty input
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return

    # Count the words
    word_count = count_words(user_input)

    # Display the result
    print(f"\nWord Count: {word_count}")

if __name__ == "__main__":
    main()
