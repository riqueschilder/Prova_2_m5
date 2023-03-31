from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Game

engine = create_engine('sqlite:///games.db')
Session = sessionmaker(bind=engine)
session = Session()

games = session.query(Game).all()

for game in games:
    print(f'Name: {game.name} | Platform: {game.platform} | Price: {game.price} | Quantity: {game.quantity}')