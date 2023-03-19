import tkinter as tk


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")

        self.current_player = "X"
        self.game_board = [" " for _ in range(9)]





        self.buttons = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", width=3, height=1, command=lambda i=i: self.click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.status_label = tk.Label(self.master, text="Current player: {}".format(self.current_player))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def click(self, i):
        if self.game_board[i] == " ":
            self.game_board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                self.status_label.config(text="{} wins!".format(winner))
                for button in self.buttons:
                    button.config(state=tk.DISABLED)
            else:
                if self.current_player == "X":
                    self.current_player = "O"
                else:
                    self.current_player = "X"
                self.status_label.config(text="Current player: {}".format(self.current_player))

    def check_winner(self):
        winning_positions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]
        for position in winning_positions:
            if self.game_board[position[0]] == self.game_board[position[1]] == self.game_board[position[2]] != " ":
                return self.game_board[position[0]]
        if " " not in self.game_board:
            return "Tie"
        return None
    


    

root = tk.Tk()
tictactoe = TicTacToe(root)
root.mainloop()
