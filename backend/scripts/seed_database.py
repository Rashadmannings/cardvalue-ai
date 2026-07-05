from app.db.database import SessionLocal
from app.models.player import Player
from app.models.grading_company import GradingCompany
from app.models.card import Card

db = SessionLocal()

# -----------------------
# Grading Companies
# -----------------------

grading_companies = [
    ("Raw", "RAW"),
    ("Professional Sports Authenticator", "PSA"),
    ("Beckett Grading Services", "BGS"),
    ("Sportscard Guaranty", "SGC"),
    ("Certified Guaranty Company", "CGC"),
]

for name, abbreviation in grading_companies:
    exists = (
        db.query(GradingCompany)
        .filter(GradingCompany.abbreviation == abbreviation)
        .first()
    )

    if not exists:
        db.add(
            GradingCompany(
                name=name,
                abbreviation=abbreviation,
            )
        )

# -----------------------
# NBA Players
# -----------------------

players = [
    "Michael Jordan",
    "LeBron James",
    "Kobe Bryant",
    "Stephen Curry",
    "Kevin Durant",
    "Victor Wembanyama",
    "Luka Doncic",
    "Anthony Edwards",
    "Giannis Antetokounmpo",
    "Caitlin Clark",
]

for player_name in players:

    exists = (
        db.query(Player)
        .filter(Player.name == player_name)
        .first()
    )

    if not exists:
        db.add(Player(name=player_name))

# -----------------------
# Basketball Cards
# -----------------------

sample_cards = [
    {
        "player_name": "Victor Wembanyama",
        "year": 2023,
        "brand": "Panini Prizm",
        "set_name": "Prizm",
        "card_number": "136",
        "parallel": "Base",
        "rookie": True,
    },
    {
        "player_name": "Michael Jordan",
        "year": 1986,
        "brand": "Fleer",
        "set_name": "Fleer Basketball",
        "card_number": "57",
        "parallel": "Base",
        "rookie": True,
    },
    {
        "player_name": "LeBron James",
        "year": 2003,
        "brand": "Topps Chrome",
        "set_name": "Topps Chrome",
        "card_number": "111",
        "parallel": "Base",
        "rookie": True,
    },
    {
        "player_name": "Kobe Bryant",
        "year": 1996,
        "brand": "Topps Chrome",
        "set_name": "Topps Chrome",
        "card_number": "138",
        "parallel": "Base",
        "rookie": True,
    },
]

for card_data in sample_cards:
    player = db.query(Player).filter(Player.name == card_data["player_name"]).first()

    if player:
        exists = (
            db.query(Card)
            .filter(
                Card.player_id == player.id,
                Card.year == card_data["year"],
                Card.brand == card_data["brand"],
                Card.set_name == card_data["set_name"],
                Card.card_number == card_data["card_number"],
                Card.parallel == card_data["parallel"],
            )
            .first()
        )

        if not exists:
            db.add(
                Card(
                    player_id=player.id,
                    year=card_data["year"],
                    brand=card_data["brand"],
                    set_name=card_data["set_name"],
                    card_number=card_data["card_number"],
                    parallel=card_data["parallel"],
                    rookie=card_data["rookie"],
                )
            )

db.commit()

print("✅ Database seeded successfully!")