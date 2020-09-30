LENGTH  = 7
DEPTH   = 6

s = ['O']*LENGTH

class Colors:

    @staticmethod
    def red(s : str) -> str:
        return f"\033[91m{s}\033[0m"

    @staticmethod
    def yellow(s : str) -> str:
        return f"\033[93m{s}\033[0m"

    @staticmethod
    def white(s : str) -> str:
        return f"\033[97m{s}\033[0m"

class Game:

    def __init__(self):
        self.matrix = [s.copy() for x in range(DEPTH)]

    def play(self,position : int,color:str):
        position -= 1
        for row in range(DEPTH-1,-1,-1):
            chip = self.matrix[row][position]
            if(chip != 'Y' and chip != 'R'):
                self.matrix[row][position] = color
                break

    def finished(self) -> str:
        #Per Row -- horizontal
        for row in self.matrix:
            char    = None
            times   = 0
            for column in row:
                if(column == 'R' or column == 'Y'):
                    if(char == column):
                        times += 1
                    else:
                        char = column
                        times = 1
                    if(times>3):
                        return char

        #Per Column -- vertical
        column  = 0
        row     = 0
        char    = None
        times   = 0
        while (column<LENGTH):
            caracter = self.matrix[row][column]
            if(caracter == 'R' or caracter == 'Y'):
                if(char == caracter):
                    times += 1
                else:
                    char = caracter
                    times = 1
                if(times>3):
                    return char
            row += 1
            if(row>=DEPTH):
                row     = 0
                char    = None
                times   = 0
                column  += 1

        #Diagonal
        

        return None

    def print(self):
        for row in self.matrix:
            stringRow = ""
            for char in row:
                if(char == 'R'):
                    stringRow += Colors.red(char)+'\t'
                elif(char == 'Y'):
                    stringRow += Colors.yellow(char)+'\t'
                else:
                    stringRow += Colors.white(char)+'\t'
            print(stringRow)

game = Game()
game.play(1,"R")
game.play(1,"R")
game.play(1,"Y")
game.play(1,"R")
game.print()