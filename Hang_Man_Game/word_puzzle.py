import random, os

# display instructions 
def display_instructions():
    filename = "wp_instructions.txt"
    file_mode = "r"
    infile = open(filename, file_mode)
    content = infile.read()
    infile.close()
    print(content)

# space out the guessed letters so we know the characters
def display_answer_sofar(guessed_letters):
    spaced_guessed_letters = " ".join(guessed_letters)
    print("The answer so far is " + spaced_guessed_letters) 

def main():
    display_instructions()
    # list of secret words
    word_list = ['apple', 'banana', 'watermelon', 'kiwi', 'pineapple', 'mango']
    # display current guess
    secret_word = random.choice(word_list)
    guessed_letters = "_" * len(secret_word)

    # prompt them to guess a letter 4 times.
    guesses_remaining = 4
    end_game = False
    while guesses_remaining > 0 and end_game == False:
        
        is_correct = 0
        end_counter = 0
        display_answer_sofar(guessed_letters)
        # prompt the user 
        user_guess = input("Guess a letter (" + str(guesses_remaining) + " guess(es) remaining): " )
        
        # we have to check if user input is == letter in secret word
        for i in range(len(secret_word)):
            # replace the word at index with the guessed secret word
            if user_guess == secret_word[i]:
                guessed_letters = guessed_letters[:i] + secret_word[i] + guessed_letters[i+1:]
                is_correct += 1 
    
        # checks if inputted incorrect answer and subtracts from remaining guesses
        if (is_correct == 0):
            guesses_remaining -= 1

        # end condition
        if (guessed_letters == secret_word):
            end_game = True
            display_answer_sofar(guessed_letters)
            print("Good job! You found the word " + secret_word + "!")
        elif (guesses_remaining == 0):
            print("Not quite, the correct word was " + secret_word + ". Better luck next time")
        


main()
