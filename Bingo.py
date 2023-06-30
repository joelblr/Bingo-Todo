#!/usr/bin/python3

#TODO : Score Board
#TODO : Two-Player or AI
#TODO : GUI

#TODO: Option for New Board, reJumble at the Start
#TODO: Show the Current Status


class BINGO :

    def __init__(self) :

        # 5x5 Grid
        self.board = [ [0 for j in range(5)] for i in range(5)]       
        # Position of the 25 Numbers (x, y)
        self.plot = {}
        # BINGO if 5
        self.bingo = 0
        # To know when one Bingo Occurs
        self.check = {
            "row" : [0, 0, 0, 0, 0],
            "column" : [0, 0, 0, 0, 0],
            "diagonal" : [0, 0],
        }


    def board_create(self) :

        import random
        choices = [num for num in range(11, 36)]

        for i in range(5) :
            for j in range(5) :

                num = random.choice(choices)
                choices.pop( choices.index(num))

                self.board[i][j] = num
                self.plot[num] = (i, j)

        return

    # TODO : In Progress !!!!!!!!!!!
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

        print("\n\t%s" % (">"*16))
        # print()
        for idx in range(5) :
            row = tuple( self.board[idx])
            print("\t|%s|%s|%s|%s|%s|" % row)
            # print("\t%s" % ("-"*16))
        print("\t%s" % ("<"*16))
        print()
        # print( self.plot)


    def board_update(self) :

        print("-"*35)

        try :
            num = int( input("Enter a Number : "))
            if (int(num) < 11 or int(num) > 35) :
                raise IOError

        except IOError :
            print("Out of Bounce: Numbers 11 to 35 only!")
            return self.board_update()

        except ValueError :
            print("Wrong Number: Numbers 11 to 35 only!")
            return self.board_update()

        except (KeyboardInterrupt, EOFError) :
            print("\nPlz Play: Numbers 11 to 35, Ezy.")
            return self.board_update()

        row, col = self.plot.get(num, 0)

        if self.board[row][col] == "**" :
            print("Same Number, Try Again !")
            return self.board_update()

        self.board[row][col] = "**"
        self.bingo_update(row, col)

        return


    def bingo_update(self, row, col) :

        self.check["row"][row] += 1
        self.check["column"][col] += 1
        if row == col == 2 :
            self.check["diagonal"][0] += 1
            self.check["diagonal"][1] += 1
        elif row == col :
            self.check["diagonal"][0] += 1
        elif row + col == 4 :
            self.check["diagonal"][1] += 1


    def bingo_check(self, name, idx) :
        for i in idx :
            if self.check[name][i] == 5 :
                self.check[name][i] = 0
                self.bingo += 1

    # XXX : return True after every check, ie when bingo == 5
    def board_validate(self) :

        self.bingo_check("row", [i for i in range(5)])
        self.bingo_check("column", [i for i in range(5)])
        self.bingo_check("diagonal", [0])
        self.bingo_check("diagonal", [1])

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

    game.board_create()
    game.board_print()

    while True :

        game.board_update()
        game.board_print()
        if game.board_winner() :
            break



# pyinstaller.exe --onefile --windowed --icon=app.ico app.py --name=app

        num = n
        while n > 1 :
            if not (factor_check(n) and factor_check(num//n)) :
                return False

            n = (n + 1) // 2
            while (n > 1 and num % n) :
                n = (n + 1) // 2
        n = num
        while n > 1 :
            if not (factor_check(n) and factor_check(num//n)) :
                return False

            n = (n + 2) // 3
            while (n > 1 and num % n) :
                n = (n + 2) // 3
        n = num
        while n > 1 :
            if not (factor_check(n) and factor_check(num//n)) :
                return False

            n = (n + 4) // 5
            while (n > 1 and num % n) :
                n = (n + 4) // 5
