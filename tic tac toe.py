def clear_screen():
    for i in range(50):
        print()


def winner():
    global game_concluded
    print("\nPlayer O, you win!")
    game_concluded = True


def win_or_draw():
    global game_concluded
    if len(list_of_all_positions) > 4:
        if "1" in list_of_o_positions and "2" in list_of_o_positions and "3" in list_of_o_positions or "4" in \
                list_of_o_positions and "5" in list_of_o_positions and "6" in list_of_o_positions or "7" in \
                list_of_o_positions and "8" in list_of_o_positions and "9" in list_of_o_positions or "1" in \
                list_of_o_positions and "4" in list_of_o_positions and "7" in list_of_o_positions or "2" in \
                list_of_o_positions and "5" in list_of_o_positions and "8" in list_of_o_positions or "3" in \
                list_of_o_positions and "6" in list_of_o_positions and "9" in list_of_o_positions or "3" in \
                list_of_o_positions and "5" in list_of_o_positions and "7" in list_of_o_positions or "1" in \
                list_of_o_positions and "5" in list_of_o_positions and "9" in list_of_o_positions or "1" in \
                list_of_x_positions and "2" in list_of_x_positions and "3" in list_of_x_positions or "4" in \
                list_of_x_positions and "5" in list_of_x_positions and "6" in list_of_x_positions or "7" in \
                list_of_x_positions and "8" in list_of_x_positions and "9" in list_of_x_positions or "1" in \
                list_of_x_positions and "4" in list_of_x_positions and "7" in list_of_x_positions or "2" in \
                list_of_x_positions and "5" in list_of_x_positions and "8" in list_of_x_positions or "3" in \
                list_of_x_positions and "6" in list_of_x_positions and "9" in list_of_x_positions or "3" in \
                list_of_x_positions and "5" in list_of_x_positions and "7" in list_of_x_positions or "1" in \
                list_of_x_positions and "5" in list_of_x_positions and "9" in list_of_x_positions:
            winner()
        else:
            if len(list_of_all_positions) == 9:
                print("\nIt's a draw!")
                game_concluded = True


def would_you_like_another_game():
    global game_concluded, terminated
    valid_y_or_n = False
    while not valid_y_or_n:
        another_game = input("\nWould you like to play again? yes/no: ").lower()
        clear_screen()
        if another_game == "yes":
            game_concluded = False
            valid_y_or_n = True
        elif another_game == "no":
            print("\nPROGRAM TERMINATED")
            terminated = True
            valid_y_or_n = True
        else:
            print("\nPlease choose yes or no only")
            valid_y_or_n = False


def get_user_input_and_update_lists():
    global list_of_all_positions, list_of_unused_numbers, valid_choice_made
    while not valid_choice_made:
        if (len(list_of_all_positions) / 2).is_integer() or len(list_of_all_positions) == 0:
            latest_o = input("\nPlayer O, please select a position for your O: ")
            if latest_o in list_of_unused_numbers and len(latest_o) != 0:
                list_of_o_positions.append(latest_o)
                list_of_all_positions = list_of_o_positions + list_of_x_positions
                list_of_unused_numbers = list_of_unused_numbers.replace(latest_o, "")
                valid_choice_made = True
            else:
                print("\nPlease choose a valid option.")
        else:
            latest_x = input("\nPlayer X, please select a position for your X: ")
            if latest_x in list_of_unused_numbers and len(latest_x) != 0:
                list_of_x_positions.append(latest_x)
                list_of_all_positions = list_of_o_positions + list_of_x_positions
                list_of_unused_numbers = list_of_unused_numbers.replace(latest_x, "")
                valid_choice_made = True
            else:
                print("\nPlease choose a valid option.")


def display_current_game():
    global updated_output
    if len(list_of_o_positions) > 0:
        for i in range(len(list_of_o_positions)):
            if list_of_o_positions[i] in updated_output:
                updated_output = updated_output.replace(list_of_o_positions[i], "O")
    if len(list_of_x_positions) > 0:
        for i in range(len(list_of_x_positions)):
            if list_of_x_positions[i] in updated_output:
                updated_output = updated_output.replace(list_of_x_positions[i], "X")
    for i in range(len(list_of_unused_numbers)):
        if list_of_unused_numbers[i] in updated_output:
            updated_output = updated_output.replace(list_of_unused_numbers[i], " ")
    clear_screen()
    print(updated_output)


terminated = False
while not terminated:
    grid_reference = "7|8|9\n-----\n4|5|6\n-----\n1|2|3"
    list_of_o_positions = []
    list_of_x_positions = []
    list_of_all_positions = []
    list_of_unused_numbers = "123456789"
    game_concluded = False

    while not game_concluded:
        updated_output = grid_reference
        print("\n" + grid_reference)
        valid_choice_made = False
        get_user_input_and_update_lists()
        display_current_game()
        win_or_draw()

    would_you_like_another_game()
