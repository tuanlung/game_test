from board import Board, Direction
from viewer import Viewer

class Game:
    def __init__(self, board_width=4, goal=2048):
        self._board = Board(board_width)
        self._board.add_new_element()
        self._board.add_new_element()
        self._viewer = Viewer(len(str(goal)))
        self._board_width = board_width
        self._goal = goal

    def main_loop(self):
        while True:
            self._viewer.draw(self._board)
            if self._board.get_max() >= self._goal:
                print("You won!")
                return

            cmd = input('Enter next sliding direciton (s/d/f/e) , "r" to restart, or "q" to leave: ')
            success = False
            if cmd == "s":
                success = self._board.slide(Direction.LEFT)
            elif cmd == "d":
                success = self._board.slide(Direction.DOWN)
            elif cmd == "f":
                success = self._board.slide(Direction.RIGHT)
            elif cmd == "e":
                success = self._board.slide(Direction.UP)
            elif cmd == "r":
                self._board = Board(self._board_width)
                self._board.add_new_element()
                self._board.add_new_element()
                print("Game restarted")
                print("")
                continue
            elif cmd == "q":
                print("Game ended")
                return
            else:
                print(f"Unknown input: {cmd}, please retry")
                continue
            if not success:
                print("Can't slide this direction: {dir}, please try other directions")
                continue
            self._board.add_new_element()

if __name__ == "__main__":
    goal_score = input("Start the game with a goal score: ")
    g = Game(goal=int(goal_score))
    g.main_loop()



