# ☠️ Grand Line Character Builder

A production-grade One Piece themed pirate crew builder REST API built with Flask, SQLAlchemy, and Streamlit.

## What it does

Build and manage your pirate crew for the Grand Line. Create characters with classes like Swordsman, Navigator, and Devil Fruit User, choose from races like Fishman, Giant, and Mink, set your bounty which scales with your level, and write your backstory.

## Project Structure
## Requirements

- Python 3.11+
- pip

## Installation

```bash
git clone https://github.com/tedybojkova/grand-line-character-builder.git
cd grand-line-character-builder
pip install -r requirements.txt
```

## Running the API

```bash
python run.py
```

API runs at `http://localhost:5000`

## Running the Frontend

Open a second terminal and run:

```bash
streamlit run frontend/app.py
```

Open `http://localhost:8501` in your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/characters/` | List all characters |
| POST | `/characters/` | Create a character |
| GET | `/characters/<id>` | Get a character by ID |
| PUT | `/characters/<id>` | Update a character |
| DELETE | `/characters/<id>` | Delete a character |
| GET | `/characters/roll` | Roll random stats |
| GET | `/classes/` | List all classes |
| GET | `/races/` | List all races |

## Running Tests

```bash
pytest
```

Coverage report is generated automatically. Current coverage: **90%**

## Code Quality

```bash
black app/
pylint app/
mypy app/
```

## Docker

```bash
docker build -t grand-line-character-builder .
docker run -p 5000:5000 grand-line-character-builder
```

## CI/CD Pipeline

GitHub Actions runs automatically on every push to `main`:

1. Installs dependencies
2. Runs pylint (minimum score 7.0)
3. Runs pytest with coverage (minimum 80%)
4. Uploads coverage report as artifact
5. Builds Docker container

## Architecture

The app follows a layered architecture:

- **Routes** — handle HTTP requests and return JSON responses
- **Services** — contain all business logic and validation
- **Models** — SQLAlchemy ORM models with computed properties
- **Exceptions** — custom exception classes for clean error handling
- **Logging** — structured logging at DEBUG and INFO levels throughout

## Classes

| Class | Hit Die | Primary Stat |
|-------|---------|--------------|
| Swordsman | d10 | Strength |
| Navigator | d6 | Intelligence |
| Sniper | d8 | Dexterity |
| Cook | d8 | Dexterity |
| Doctor | d8 | Wisdom |
| Devil Fruit User | d6 | Charisma |
| Shipwright | d10 | Constitution |
| Musician | d6 | Charisma |
| Archaeologist | d6 | Intelligence |
| Pirate Captain | d8 | Charisma |
| Marine | d10 | Strength |
| Bounty Hunter | d10 | Dexterity |

## Races

| Race | Bonuses |
|------|---------|
| Human | +1 to all stats |
| Fishman | STR +2, CON +2 |
| Giant | STR +3, CON +2, CHA -1 |
| Mink | DEX +2, WIS +1 |
| Cyborg | CON +3, INT +1, CHA -2 |
| Lunarian | STR +1, DEX +1, CON +3 |
| Longarm Tribe | DEX +3, INT +1 |
| Longleg Tribe | DEX +2, STR +1 |
| Tontatta | DEX +3, WIS +1, STR -1 |
| Skypiean | WIS +2, DEX +1 |

## Technologies

- **Flask** — REST API framework
- **SQLAlchemy** — ORM and database management
- **Streamlit** — frontend UI
- **pytest + pytest-cov** — testing and coverage
- **pylint + mypy + black** — code quality tools
- **Sphinx** — API documentation generation
- **Docker** — containerisation
- **GitHub Actions** — CI/CD pipeline

## Author

Teodora Bozhkova — [@tedybojkova](https://github.com/tedybojkova)