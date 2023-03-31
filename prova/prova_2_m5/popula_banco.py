from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Game

engine = create_engine('sqlite:///games.db')
Session = sessionmaker(bind=engine)
session = Session()

games = [
    Game(name='DEAD SPACE REMAKE', platform='PS5', price=350.00, quantity=10),
    Game(name='FORSPOKEN', platform='PC', price=299.00, quantity=8),
    Game(name='DEAD ISLAND 2', platform='PS5', price=350.00, quantity=10),
    Game(name='HOGWARTS LEGACY', platform='PC', price=219.00, quantity=7),
    Game(name='WILD HEARTS', platform='XBox Series', price=350.00, quantity=7),
    Game(name='RESIDENT EVIL 4', platform='PS5', price=289.00, quantity=10),
    Game(name='THE LEGEND OF ZELDA: TEARS OF THE KINGDOM', platform='Switch', price=350.00, quantity=10)
]

for game in games:
    session.add(game)

session.commit()