grid = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

def print_grid():
    for row in range(len(grid[row])):
        for col in range(row):
            print(grid[row][col], end="")
            if (col != 2 ):
                print("|", end="")
        print()
        if(row != 2):
            print("*****")
        
        

def game_loop():
    print("Welcome to tic tac toe")
    while(True):
        user_request = input("Enter STOP to end or anything else to continue!")
        if user_request.__eq__("STOP"):
            break
    print("GAME IS OVER!")




game_loop()
