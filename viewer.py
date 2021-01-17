from board import Board

class Viewer:
    def __init__(self, max_digit=4):
        self._max_digit = max_digit

    def draw(self, b):
        print("Board Visualization:")
        for r in b.board:
            line = ["|"]
            for c in r:
                if c == None:
                    line.append("-"*self._max_digit)
                else:
                    line.append(f"{c:{self._max_digit}}")
                line.append("|")
            print(" ".join(line))
        print("")
                


