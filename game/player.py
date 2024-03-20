import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        """
        Initialize a Player object.

        Parameters:
        x (int): The x-coordinate of the player.
        y (int): The y-coordinate of the player.
        width (int): The width of the player.
        height (int): The height of the player.
        color (tuple): The color of the player. Expects an RGB tuple.
        """
        self.rect = pygame.Rect(x, y, width, height)  # Player's rectangle
        self.color = color  # Player's color
        self.vel = 3  # Player's velocity

    def draw(self, win):
        """
        Draw the player on the specified window.

        Parameters:
        win (Surface): The pygame surface to draw the player on.
        """
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        """
        Update the player's position based on pressed keys.

        Moves the player in response to arrow key inputs. Uses the player's
        velocity attribute to determine the distance moved in each direction.
        """
        keys = pygame.key.get_pressed()
        for key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            if keys[key]:
                if key == pygame.K_LEFT:
                    self.rect.x -= self.vel
                elif key == pygame.K_RIGHT:
                    self.rect.x += self.vel
                elif key == pygame.K_UP:
                    self.rect.y -= self.vel
                elif key == pygame.K_DOWN:
                    self.rect.y += self.vel
