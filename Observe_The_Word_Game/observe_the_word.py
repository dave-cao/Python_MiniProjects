import time, os, random

continue_game = True
while (continue_game):
    # clear screen
    clear_command = "clear"
    if (os.name == "nt"):
        clear_command = "cls"
    os.system(clear_command)

    # display header
    header_border = "-" * 80
    header_content = "Remember The Word"
    print(header_border)
    print(header_content)
    print(header_border)

    # display instructions

    filename = "instructions.txt"
    file_mode = "r"
    infile = open(filename, file_mode)
    content = infile.read()
    infile.close()
    print(content)

    # prompt player to press enter and clear screen after
    input("Press enter key to display the words.")
    os.system(clear_command)
    print(header_border)
    print(header_content)
    print(header_border)

    # display four words
    filename = "words.txt"
    file_mode = "r"
    infile = open(filename, file_mode)
    all_words = infile.read()
    all_words_list = all_words.splitlines()
    words = random.sample(all_words_list, 4)

    answer = random.choice(words)
    start_letter = answer[0]

    pause_time = 1
    for word in words:
        print(word)
        time.sleep(pause_time)
        os.system(clear_command)
        # display header
        print(header_border)
        print(header_content)
        print(header_border)

    # prompt player to enter a word that starts with a particular letter
    guess = input("What word starts with the letter " + start_letter + "? ")

    #evaluate answer and display feedback
    if (guess.lower() == answer.lower()):
        print('Congratulations, you are corect.')
    else:
        print('Sorry you entered '+guess+'.')
        print('The answer was ' + answer + ".")

    # prompt player to play again
    reply = input("Play again? y/n ").lower()
    continue_game = reply == "y"