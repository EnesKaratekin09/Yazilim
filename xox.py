import random
pl_win=0
pc_win=0
def print_board(board):
    print(" {} | {} | {} \n {} | {} | {} \n {} | {} | {} ".format(*board))

def game():
    global pl_win, pc_win
    move_list = ["1","2","3","4","5","6","7","8","9"]
    valid_move = ["1","2","3","4","5","6","7","8","9"]
    win=""
    def win_check():
        if move_list[0] == move_list[1] == move_list[2] == "X" or \
           move_list[3] == move_list[4] == move_list[5] == "X" or \
           move_list[6] == move_list[7] == move_list[8] == "X" or \
           move_list[0] == move_list[3] == move_list[6] == "X" or \
           move_list[1] == move_list[4] == move_list[7] == "X" or \
           move_list[2] == move_list[5] == move_list[8] == "X" or \
           move_list[0] == move_list[4] == move_list[8] == "X" or \
           move_list[2] == move_list[4] == move_list[6] == "X":
               return "You"
    
        elif move_list[0] == move_list[1] == move_list[2] == "O" or \
             move_list[3] == move_list[4] == move_list[5] == "O" or \
             move_list[6] == move_list[7] == move_list[8] == "O" or \
             move_list[0] == move_list[3] == move_list[6] == "O" or \
             move_list[1] == move_list[4] == move_list[7] == "O" or \
             move_list[2] == move_list[5] == move_list[8] == "O" or \
             move_list[0] == move_list[4] == move_list[8] == "O" or \
             move_list[2] == move_list[4] == move_list[6] == "O":
                 return "Computer"
        else:
            return ""
        
    while True:
        game_start = input("Do you wanting to play XOX?\nyes(Y)/no(N)\n").strip().upper()
        if game_start == "Y":
            break
        elif game_start == "N":
            print("Quitting.")
            quit()
        else:
            print("Invalid input. Please enter Y or N.")

    while True:
        print_board(move_list)
        plc = input("\nEnter your choice (1-9, q to quit): ").strip()

        if not plc:  
            print("You must enter a number.")
            continue
    
        if plc.lower() == "q":
            print("Game terminated.")
            quit()

        if plc not in valid_move:
            print("Invalid choice. Please pick an empty square.")
            continue

        move_list[int(plc)-1] = "X"
        valid_move.remove(plc)
        
        win = win_check()
        if win == "You":
            print_board(move_list)
            pl_win+=1
            print("You win!")
            print(f"You {pl_win} - {pc_win} Computer")
            game()
            
        if not valid_move:  
            print_board(move_list)
            print("Game end. Board full.\nDraw.")
            game()
            
        aic = random.choice(valid_move)
        move_list[int(aic)-1] = "O"
        valid_move.remove(aic)
        
        win = win_check()
        if win == "Computer":
            print_board(move_list)
            pc_win+=1
            print("Computer wins!")
            print(f"You {pl_win} - {pc_win} Computer")
            game()

        if not valid_move:  
            print_board(move_list)
            print("Game end. Board full.Draw.")
            game()
game()
