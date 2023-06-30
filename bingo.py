#!/usr/bin/python3

#TODO : Convert 2D to 1D Board
#TODO : Score Board
#TODO : Two-Player or AI
#TODO : GUI 


class BINGO :

    def __init__(self) :

        self.board = []
        self.hmap = {}
        self.bingo = 0
        self.pattern = "*" * 10

        self.row, self.col = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
        self.diagonal = [0, 0]
        # self.moves = set()
        # self.turn = 1


    # XXX : Doesnt check if within range <1 to 25>
    def board_input(self) :


        print(f'\n{"-"*35}')
        print("Enter 11 to 35 Numbers Row Wise.")
        print("5 Nums in Each Row Space-Separated\n")

        idx = 0
        for i in range(1, 6) :
            rowInput = input(f"Row {i} : ").split()
            self.board += rowInput
            for nums in rowInput :
                self.hmap[nums] = idx
                idx += 1
        print()


    def board_print(self) :

        print("\n\t%s" % ("-"*16))
        for idx in range(0, 25, 5) :
            row = tuple( self.board[idx : idx + 5])
            print("\t|%s|%s|%s|%s|%s|" % row)
            print("\t%s" % ("-"*16))
        print()
        print( self.hmap)

    def board_update(self) :

        print("-"*35)

        try :
            num = str( int( input("Enter a Number : ")))

        except :
            print("Wrong Input, Try Again !")
            return self.board_update()

        key = self.hmap.get(num, 0)
        if (int(num) < 11 or int(num) > 35) :
            print("Wrong Input, Try Again !")
            return self.board_update()

        elif self.board[key] == "**" :
            print("Same Input, Try Again !")
            return self.board_update()

        self.board[key] = "**"

        return


    # XXX : return True after every check, ie when bingo == 5
    def board_validate(self) :

        #row
        col = ["" for _ in range(5)]
        for idx in range( len(self.row)) :
            if not self.row[idx] :
                if "".join( self.board[idx * 5 : (idx + 1) * 5]) == self.pattern :
                    self.bingo += 1
                    self.row[idx] = 1

            col = [col[_] + self.board[idx * 5 + _]   for _ in range(5)]

        #col
        for idx in range( len(self.col)) :
            if not self.col[idx] :
                if col[idx] == self.pattern :
                    self.bingo += 1
                    self.col[idx] = 1

        #dia
        diagonal1 = "".join( [self.board[_] for _ in range(0, 25, 6)])
        if not self.diagonal[0] and diagonal1 == self.pattern :
            self.bingo += 1
            self.diagonal[0] = 1

        diagonal2 = "".join( [self.board[_] for _ in range(4, 21, 4)])
        if not self.diagonal[1] and diagonal2 == self.pattern :
            self.bingo += 1
            self.diagonal[1] = 1

        return self.bingo >= 5


    def board_winner(self) :

        winner = self.board_validate()
        if winner :
            print("\nB-I-N-G-O\nYou Won!")
            print(f'{"-"*35}\n')
            return 1
        return 0


if __name__ == "__main__" :

    game = BINGO()

    game.board_input()
    game.board_print()

    while True :

        game.board_update()
        game.board_print()
        if game.board_winner() :
            break



# pyinstaller.exe --onefile --windowed --icon=app.ico app.py --name=app

