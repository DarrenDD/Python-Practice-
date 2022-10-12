

grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]


def main():
    display_title()
    display_grid()
    start_game()
    

def display_title():
    print("\n Welcome to the Tic Tac Toe Game!")
    
def start_game():
    game_over = False
    while not game_over:
        game_over = take_turn()
        print()
        print("Game Over")
        
def take_turn():
    turns = 1
    while True:
        if not turns % 2 == 0:
            player = 'X'
        else:
            player = 'O'
        print(f"{player}'s turn")
        
        row = int(input("Pick a row (1, 2, 3): "))
        if row < 1 or row > 3:
            print("Invalid row number - try again!")
            continue
        
        column = int(input("Pick a column (1, 2, 3): "))
        if column < 1 or column > 3:
            print("Invalid column number - try again!")
            continue
        
        if not [row-1][column-1] == " ":
            print("Spot has been taken")
            continue
        
        grid[row-1][column-1] = player
        display_grid()
        
        
        winner = check_winner()
        if winner == 'X' or winner == 'O':
            print(f"{winner}: wins")
            game_over = True
            return game_over
        
        if turns == 9:
            print("Its a TIE!")
            game_over = True
            return game_over
        
        turns += 1

def display_grid():
    print()
    print("+---+---+---+")
    for row in grid:
        print("|", end = "")
        for column in row:
            print(f" {column} |", end = "")
        print()
        print("+---+---+---+")
    print()


def check_winner():
    #check rows
    for x in range(3):
        if grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2]:
            return grid[x][0] 
    #check columns
    for y in range(3):
        if grid[0][y] == grid[1][y] and grid[1][y] == grid[2][y]:
            return grid[0][y]
    
    #check diagonal 1    
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]
    #check diagonal 2    
    if grid[2][2] == grid[1][1] and grid[1][1] == grid[0][0]:
        return grid[0][0]
    
    #no winner yet
    return " "

if __name__ == '__main__':
    main()    