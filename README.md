# chess-gaming
Chess Game &amp; Player Database



# Chess Game & Player Database

## Project Description
A Django-based web application that provides a REST API for managing chess games and player data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:Mirxojiddin/chess-gaming.git
   cd chess-gaming
   ```
2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   python manage.py migrate
   python manage.py generate_data  # Custom management command to generate data
   ```
4. Run server
```bash
  python manage.py runserver
```
## Usage
Access the application at http://127.0.0.1:8000/

## API Documentation
Sure! Here's the API documentation for the Players and Games endpoints written in Markdown format:

```markdown
# Players Endpoint

## Get All Players

- **URL:** `/api/players/`
- **Method:** GET
- **Description:** Retrieve a list of all players.
- **Response:** JSON

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "elo_rating": 2100,
    "country": "USA",
    "games_played": 50,
    "wins": 30,
    "losses": 15,
    "draws": 5
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "elo_rating": 2200,
    "country": "UK",
    "games_played": 60,
    "wins": 40,
    "losses": 10,
    "draws": 10
  }
]
```

## Filter Players

- **URL:** `/api/players/`
- **Method:** GET
- **Description:** Retrieve a list of players based on filter criteria.
- **Query Parameters:**
  - `name` (string, optional): Filter players by name.
  - `elo_rating_min` (integer, optional): Filter players with a minimum ELO rating.
  - `elo_rating_max` (integer, optional): Filter players with a maximum ELO rating.
  - `country` (string, optional): Filter players by country.
- **Example Request:**
  ```
  GET /api/players/?name=John&elo_rating_min=2000&elo_rating_max=2500&country=USA
  ```
- **Example Response:** JSON

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "elo_rating": 2100,
    "country": "USA",
    "games_played": 50,
    "wins": 30,
    "losses": 15,
    "draws": 5
  }
]
```

## Create a New Player

- **URL:** `/api/players/`
- **Method:** POST
- **Description:** Create a new player.
- **Request Body:** JSON

```json
{
  "name": "Alice Johnson",
  "elo_rating": 1800,
  "country": "Canada",
  "games_played": 0,
  "wins": 0,
  "losses": 0,
  "draws": 0
}
```

- **Response:** JSON

```json
{
  "id": 3,
  "name": "Alice Johnson",
  "elo_rating": 1800,
  "country": "Canada",
  "games_played": 0,
  "wins": 0,
  "losses": 0,
  "draws": 0
}
```

## Update a Player

- **URL:** `/api/players/{id}/`
- **Method:** PUT
- **Description:** Update an existing player.
- **Request Body:** JSON

```json
{
  "name": "Alice Johnson",
  "elo_rating": 1850,
  "country": "Canada",
  "games_played": 10,
  "wins": 5,
  "losses": 4,
  "draws": 1
}
```

- **Response:** JSON

```json
{
  "id": 3,
  "name": "Alice Johnson",
  "elo_rating": 1850,
  "country": "Canada",
  "games_played": 10,
  "wins": 5,
  "losses": 4,
  "draws": 1
}
```

## Delete a Player

- **URL:** `/api/players/{id}/`
- **Method:** DELETE
- **Description:** Delete an existing player.
- **Response:** JSON

```json
{
  "detail": "Player deleted successfully."
}
```

## Filtering Examples

### Example 1: Filter by Name

- **Request:**
  ```
  GET /api/players/?name=Alice
  ```
- **Response:** JSON

```json
[
  {
    "id": 3,
    "name": "Alice Johnson",
    "elo_rating": 1850,
    "country": "Canada",
    "games_played": 10,
    "wins": 5,
    "losses": 4,
    "draws": 1
  }
]
```

### Example 2: Filter by ELO Rating Range

- **Request:**
  ```
  GET /api/players/?elo_rating_min=2000&elo_rating_max=2500
  ```
- **Response:** JSON

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "elo_rating": 2100,
    "country": "USA",
    "games_played": 50,
    "wins": 30,
    "losses": 15,
    "draws": 5
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "elo_rating": 2200,
    "country": "UK",
    "games_played": 60,
    "wins": 40,
    "losses": 10,
    "draws": 10
  }
]
```

### Example 3: Filter by Country

- **Request:**
  ```
  GET /api/players/?country=USA
  ```
- **Response:** JSON

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "elo_rating": 2100,
    "country": "USA",
    "games_played": 50,
    "wins": 30,
    "losses": 15,
    "draws": 5
  }
]
```

### Example 4: Combined Filters

- **Request:**
  ```
  GET /api/players/?name=Jane&elo_rating_min=2000&country=UK
  ```
- **Response:** JSON

```json
[
  {
    "id": 2,
    "name": "Jane Smith",
    "elo_rating": 2200,
    "country": "UK",
    "games_played": 60,
    "wins": 40,
    "losses": 10,
    "draws": 10
  }
]
```

# Games Endpoint

## Get All Games

- **URL:** `/api/games/`
- **Method:** GET
- **Description:** Retrieve a list of all games.
- **Response:** JSON

```json
[
  {
    "id": 1,
    "white_player": "John Doe",
    "black_player": "Jane Smith",
    "result": "win",
    "opening_type": "Sicilian Defense",
    "number_of_moves": 42,
    "date_played": "2023-05-01"
  },
  {
    "id": 2,
    "white_player": "Alice Johnson",
    "black_player": "John Doe",
    "result": "draw",
    "opening_type": "Ruy Lopez",
   

 "number_of_moves": 30,
    "date_played": "2023-06-15"
  }
]
```

## Filter Games

- **URL:** `/api/games/`
- **Method:** GET
- **Description:** Retrieve a list of games based on filter criteria.
- **Query Parameters:**
  - `white_player_name` (string, optional): Filter games by white player name.
  - `black_player_name` (string, optional): Filter games by black player name.
  - `result` (string, optional): Filter games by result (win, loss, draw).
  - `opening_type` (string, optional): Filter games by opening type.
  - `date_played_min` (date, optional): Filter games played after this date.
  - `date_played_max` (date, optional): Filter games played before this date.
- **Example Request:**
  ```
  GET /api/games/?white_player_name=John&result=win&opening_type=Sicilian Defense&date_played_min=2023-01-01&date_played_max=2023-12-31
  ```
- **Example Response:** JSON

```json
[
  {
    "id": 1,
    "white_player": "John Doe",
    "black_player": "Jane Smith",
    "result": "win",
    "opening_type": "Sicilian Defense",
    "number_of_moves": 42,
    "date_played": "2023-05-01"
  }
]
```

## Create a New Game

- **URL:** `/api/games/`
- **Method:** POST
- **Description:** Create a new game.
- **Request Body:** JSON

```json
{
  "white_player": "Alice Johnson",
  "black_player": "John Doe",
  "result": "draw",
  "opening_type": "Ruy Lopez",
  "number_of_moves": 30,
  "date_played": "2023-06-15"
}
```

- **Response:** JSON

```json
{
  "id": 2,
  "white_player": "Alice Johnson",
  "black_player": "John Doe",
  "result": "draw",
  "opening_type": "Ruy Lopez",
  "number_of_moves": 30,
  "date_played": "2023-06-15"
}
```

## Update a Game

- **URL:** `/api/games/{id}/`
- **Method:** PUT
- **Description:** Update an existing game.
- **Request Body:** JSON

```json
{
  "white_player": "Alice Johnson",
  "black_player": "John Doe",
  "result": "win",
  "opening_type": "Ruy Lopez",
  "number_of_moves": 28,
  "date_played": "2023-06-15"
}
```

- **Response:** JSON

```json
{
  "id": 2,
  "white_player": "Alice Johnson",
  "black_player": "John Doe",
  "result": "win",
  "opening_type": "Ruy Lopez",
  "number_of_moves": 28,
  "date_played": "2023-06-15"
}
```

## Delete a Game

- **URL:** `/api/games/{id}/`
- **Method:** DELETE
- **Description:** Delete an existing game.
- **Response:** JSON

```json
{
  "detail": "Game deleted successfully."
}
```

# Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you want to make.
```

Feel free to adjust the formatting or add more details as needed!
