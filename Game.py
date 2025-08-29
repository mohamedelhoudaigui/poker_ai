class Game:
    def __init__(self):
        self.board = [[-1 for _ in range(3)] for _ in range(3)]

    def declare_win(self, c):
        self.show_board()
        print(f'Player {c} wins!')
        exit(0)

    def check_winning(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != -1:
                self.declare_win(self.board[i][0])
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != -1:
                self.declare_win(self.board[0][i])
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != -1:
            self.declare_win(self.board[1][1])
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != -1:
            self.declare_win(self.board[2][0])

    def show_board(self):
        for row in self.board:
            print('|'.join([' ' if cell == -1 else str(cell) for cell in row]))

    def Gameloop(self):
        i = 0
        while True:
            print('----------TicTacToe game--------')
            print('Player 1 is X, Player 2 is O')
            self.show_board()

            current_player = 1 if i % 2 == 0 else 2
            print(f"Player {current_player}'s turn")
            i += 1

            input_c = 1 if current_player == 1 else 0

            move = input("Enter your move as 'row,col' (e.g., 1,2): ")
            try:
                row, col = map(int, move.split(','))
                if 0 <= row < 3 and 0 <= col < 3:  # Ensure row and col are within bounds
                    if self.board[row][col] == -1:
                        self.board[row][col] = input_c
                    else:
                        print("Invalid move! Cell already occupied.")
                else:
                    print("Invalid move! Row and column must be between 0 and 2.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter row and column as 'row,col' (e.g., 1,2).")

            self.check_winning()

g = Game()
g.Gameloop()