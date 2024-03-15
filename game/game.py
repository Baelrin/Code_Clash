class Game:
    def __init__(self, id):
        """
        Initialize the game session with unique id, moves, and score keeping.
        :param id: Int identifier for the game session.
        """
        self.p1Went = False  # Tracks if player 1 has made a move
        self.p2Went = False  # Tracks if player 2 has made a move
        self.ready = False  # Indicates if the game is ready to start
        self.id = id  # Game session ID
        self.moves = [None, None]  # Moves of player 1 and 2
        self.wins = [0, 0]  # Wins count for player 1 and 2
        self.ties = 0  # Count of ties

    def get_player_move(self, p):
        """
        Returns the move made by a player.
        :param p: Player identifier (0 for player 1, 1 for player 2)
        :return: Move made by the player
        """
        return self.moves[p]

    def play(self, player, move):
        """
        Record a player's move and mark them as having made a move.
        :param player: The player making the move (0 for player 1, 1 for player 2)
        :param move: The move being made by the player
        """
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        """
        Check if the game is ready to start.
        :return: Boolean indicating if the game is ready.
        """
        return self.ready

    def bothWent(self):
        """
        Checks if both players have made their moves.
        :return: Boolean indicating if both players have moved.
        """
        return self.p1Went and self.p2Went

    def winner(self):
        """
        Determines the winner of the game based on the moves made by the players.
        :return: The winner (0 for player 1, 1 for player 2, -1 for no winner/tie)
        """
        p1 = (
            self.moves[0].upper()[0] if self.moves[0] is not None else None
        )  # Player 1's move
        p2 = (
            self.moves[1].upper()[0] if self.moves[1] is not None else None
        )  # Player 2's move
        winner = -1  # Default to no winner
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        """
        Resets the player move status to False for the next round.
        """
        self.p1Went = False
        self.p2Went = False
