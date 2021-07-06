from config.game_loop import GameLoop


class Main:
    game_loop: GameLoop

    def __init__(self):
        self.game_loop = GameLoop()

        self.start()

    def start(self):
        self.game_loop.loop()


if __name__ == '__main__':
    Main()
