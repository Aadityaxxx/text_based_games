# A text based tic_tac_toe game.
import itertools

# here player_id is for players, suppose two players are playing then their id's would be 1 and 2 respectively and those id's would be printed on game on player's move
# when we just want to see game then player_id would be zero.
def game_board(game_map, player_id = 0, row= 0, column= 0, just_display = False):

    try:
        if game_map[row][column] != 0:  #when somebody is already played at that position.
            print("Its already played there. Choose another position!")
            return game_map, False

        # dynamic header row
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))   #to print header row for position mentioning. i.e. '   0  1  2'. tip: .join() applicable on list format.

        if not just_display:   #when player_id is not 0 i.e. when we want to play the game.
            game_map[row][column] = player_id  #this will put player_id on game where its played.
        for count, row in enumerate(game): #enumerate will give us indices of elements on which we are looping through.
            print(count, row)

        return game_map, True

    except Exception as e:  #for any error.
        print("Something went wrong: ", e)
        return game_map, False


def win(game_map):
    # For Horizontal Winner
    for row in game_map:
        if row.count(row[0]) == len(row) and row[0] != 0:  #logic to check if all elements in a row are same but not all 0.
            print("Player {} won by horizontal win!".format(row[0]))
            return True  #when there is a win

    # For Vertical Winner.
    for col in range(len(game_map)):  #each time while looping we are creating a check list.
        check = []

        for row in game_map:
            check.append(row[col])  #appending all values from vertical column to check list.

        if check.count(check[0]) == len(check) and check[0] != 0: #checking for all elements in check list are same but not zero.
            print("Player {} won by vertical win!".format(check[0]))
            return True  # when there is a win

    # For Diagonal Winner
    '''there are only two diagonal ways, so we need to check those two ways.'''
    # first diagonal way: from top left to bottom right.
    # we will append all first diagonal way elements in diags_1
    diags_1 = []
    for i in range(len(game_map)):
        diags_1.append(game_map[i][i])

    # For diags_1: when all elements in diags_1 are same but not zero.
    if diags_1.count(diags_1[0]) == len(diags_1) and diags_1[0] != 0:
        print("Player {} won by diagonal win.".format(diags_1[0]))
        return True  # when there is a win

    # second diagonal way: from top right to bottom left.
    # we will append all second diagonal way elements to diags_2
    diags_2 = []
    for row, col in enumerate(
            reversed(range(len(game_map)))):  # to get second diagonal way elements row and column pos.
        diags_2.append(game_map[row][col])

    # For diags_2: when all elements in diags_2 are same but not zero.
    if diags_2.count(diags_2[0]) == len(diags_2) and diags_2[0] != 0:
        print("Player {} won by diagonal win.".format(diags_2[0]))
        return True  # when there is a win

    return False #Finally if there wasn't any win it returns False.

# game loop
play = True
while play:
    # For dynamic game size.
    game_size = int(input("What size should game be?(ex. for 3x3 type 3): "))
    game = []
    for num in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        game.append(row)


    game_won = False

    game, _ = game_board(game, just_display=True)  #just to display game board before game starts.
    player_choices = itertools.cycle([1, 2])  #iterator to alternate player 1 and player 2.


    while game_won != True:  #till nobody wins.
        current_player = next(player_choices)  # to get next player id.
        print("Current Player: {}".format(current_player))

        played = False

        while not played:

            # For bad input values.
            try:
                row_choice = int(input("Row Choice(0/1/2): "))
                col_choice = int(input("Column Choice(0/1/2): "))
                game, played = game_board(game, current_player, row_choice, col_choice)
                print('------------------------------')  # separator bet. player moves

            except Exception as e:
                print("Invalid input: ", e)

        # Input system to ask to play again.
        if win(game):  #when player wins.
            game_won = True

            again_input = input("Game is Over, would you like to play again?(y/n):")
            if again_input.lower() == 'y':
                print("Restarting...")

            elif again_input.lower() != 'y':
                print("Okay bitch, see you next time!")
                play = False  #to break out of game loop.
