# Code_Clash

Code_Clash is a multiplayer game application developed in Python, utilizing the Pygame library for the game client and a custom server implementation for managing game sessions. The game is designed to be played over a network, allowing players to compete against each other in real-time.

## Features

- **Multiplayer Support**: Code_Clash supports up to two players per game session, with the ability to create new games or join existing ones.
- **Custom Networking**: The game uses a custom server and client implementation for network communication, ensuring a smooth and responsive gaming experience.
- **Game Logic**: The core game logic, including move validation and determining the winner, is implemented in a separate module, ensuring clean and maintainable code.
- **Player Interface**: The game client features a simple and intuitive interface, including buttons for making moves and displaying game status.
- **Error Handling**: The application includes robust error handling for network communication, ensuring a stable gaming experience even in the face of network issues.

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Baelrin/Code_Clash.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Code_Clash
   ```

3. Install Pygame:

   ```bash
   pip install pygame
   ```

4. Run the server:

   ```bash
   python game/server.py
   ```

5. Run the client:

   ```bash
   python game/client.py
   ```

## Usage

- **Starting a Game**: Players can start a new game by connecting to the server. The server will automatically assign players to games as they connect.
- **Making Moves**: Players can make moves by clicking on the corresponding buttons in the game client.
- **Viewing Game Status**: The game client displays the current game status, including the winner of each round.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
