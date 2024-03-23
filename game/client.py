import socket

import pygame
from network import Network

pygame.font.init()

width = 700  # Width of the game window
height = 700  # Height of the game window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


class Button:
    """Represents a clickable button on the screen."""

    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        """Draw the button on the window."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, True, (255, 255, 255))
        win.blit(
            text,
            (
                self.x + round(self.width / 2) - round(text.get_width() / 2),
                self.y + round(self.height / 2) - round(text.get_height() / 2),
            ),
        )

    def click(self, pos):
        """Check if the button is clicked based on the mouse position."""
        x1 = pos[0]
        y1 = pos[1]
        return (
            self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height
        )


def redrawWindow(win, game, p):
    """Clears the game window, preparing it for a new frame."""
    win.fill((128, 128, 128))


def handle_network_errors(n):
    """Handle errors that might occur during network communication."""
    try:
        game = n.send("get")
    except socket.error:
        print("Network error")
        return None
    except Exception as e:
        print("Couldn't get game", e)
        return None
    return game


def handle_game_events(game, player, n):
    """Process game events, including resetting the game after each round."""
    if game is not None and game.bothWent():
        redrawWindow(win, game, player)
        pygame.time.delay(500)
        try:
            game = n.send("reset")
        except socket.error:
            print("Network error")
            return None
        except Exception as e:
            print("Couldn't get game", e)
            return None
    return game


def update_interface(win, game, player):
    """Update the game interface based on the game state."""
    font = pygame.font.SysFont("comicsans", 90)
    if game is None:
        text = font.render("Game not available", True, (255, 0, 0))
    elif (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
        text = font.render("You Won!", True, (255, 0, 0))
    elif game.winner() == -1:
        text = font.render("Tie Game!", True, (255, 0, 0))
    else:
        text = font.render("You Lost...", True, (255, 0, 0))
    win.blit(
        text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2)
    )
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    """Main game loop."""
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(str(n.getP())) if n.getP() is not None else 0
    print("You are player", player)

    while run:
        clock.tick(60)
        game = handle_network_errors(n)
        if game is not None:
            game = handle_game_events(game, player, n)
            update_interface(win, game, player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in btns:
                    if (
                        game is not None
                        and game.connected()
                        and (
                            player == 0
                            and not game.p1Went
                            or player != 0
                            and not game.p2Went
                        )
                    ):
                        n.send(btn.text)
        redrawWindow(win, game, player)


btns = [
    Button("Rock", 50, 500, (0, 0, 0)),
    Button("Scissors", 250, 500, (255, 0, 0)),
    Button("Paper", 450, 500, (0, 255, 0)),
]

while True:
    main()
