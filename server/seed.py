#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet

with app.app_context():
    pets = []
    pets.append(Pet(name="Fido", species="Dog"))
    pets.append(Pet(name="Whiskers", species="Cat"))
    pets.append(Pet(name="Hermie", species="Hamster"))
    db.session.add_all(pets)
    db.session.commit()