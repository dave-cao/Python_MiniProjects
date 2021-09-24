import random

# global variables
player_one_overall_score = 0
player_two_overall_score = 0
overall_ties = 0
call_choices = ["H", "T"]

# helper function - find number of HH sequences in list
def HH_sequence_count_function(player_list):
    i = 0
    sequence_count = 0
    while (i < len(player_list) - 1):
        current = player_list[i]
        next = player_list[i + 1]
        if (current == "H" and next == "H"):
            sequence_count += 1
        i += 1
    return sequence_count

def main(player_one_overall_score, player_two_overall_score, overall_ties):
    # display instructions
    filename = "instructions.txt"
    file_mode = "r"
    infile = open(filename, file_mode)
    content = infile.read()
    infile.close()
    print(content)

    # game variables
    player_one_score = 0
    player_two_score = 0
    game_round = 0
    end_round = 4

    player_one_toss_list = []
    player_two_toss_list = []

    # continously calls the game until end game
    while (game_round < end_round):
        user_call = input("Heads or Tails? Type H or T: ")
        player_one_toss = random.choice(call_choices)
        player_two_toss = random.choice(call_choices)

        # add toss into list
        player_one_toss_list.append(player_one_toss)
        player_two_toss_list.append(player_two_toss)

        print("Player 1 has tossed", player_one_toss)
        print("Player 2 has tossed", player_two_toss)

        if (player_one_toss == user_call):
            player_one_score += 1
            print("Player 1 wins")
        if (player_two_toss == user_call):
            player_two_score += 1
            print("Player 2 wins")
        game_round += 1

    # end stats 
    print("ROUND STATS")
    if (player_one_score > player_two_score):
        player_one_overall_score += 1
        print("Player 1 wins this round")
    elif (player_two_score > player_one_score):
        player_two_overall_score += 1
        print("Player 2 wins this round")
    else:
        overall_ties += 1
        print("Too bad, no one wins the game.")

    print("Player 1 points:", player_one_score)
    print("Player 2 points:", player_two_score)

    print("Player 1 tossed", player_one_toss_list)
    print("Player 2 tossed", player_two_toss_list)

    # check sequence for HH
    print("H H found in the player 1 sequence", HH_sequence_count_function(player_one_toss_list))
    print("H H found in the player 2 sequence", HH_sequence_count_function(player_two_toss_list))

    # play again?
    play_again = input("Do you want to play another round? y/n ")
    if (play_again == "y"):
        main(player_one_overall_score, player_two_overall_score, overall_ties)
    else:
        print("SUMMARY STATS")
        print("Number of ties:", overall_ties)
        print("Number of player 1 wins:", player_one_overall_score)
        print("Number of player 2 wins:", player_two_overall_score)


main(player_one_overall_score, player_two_overall_score, overall_ties)
