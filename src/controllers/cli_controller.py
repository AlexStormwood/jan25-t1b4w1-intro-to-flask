from flask import Blueprint
from src.init import db

from src.models.user import User
from src.models.article import Article

# Declare a Blueprint for database commands.
# This thing will be given all CLI functionality
# and then loaded by the main app in app.py.
db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
	"""Create the database tables."""
	db.create_all()
	print("Database tables created.")

@db_commands.cli.command('drop')
def drop_db():
	"""Drop the database tables."""
	db.drop_all()
	print("Database tables dropped.")

@db_commands.cli.command('seed')
def seed_db():
	"""Seed the database with initial data."""
	# Create some users
	users = [
		User(username='alice', email='test@email.com'),
		User(username='bob', email='test2@email.com'),
	]
	db.session.add_all(users)
	db.session.commit()

	# Create some articles
	articles = [
		Article(title='First Article', content='Content of the first article', author_id=users[0].id),
		Article(title='Second Article', content='Content of the second article', author_id=users[1].id),
	]
	db.session.add_all(articles)
	db.session.commit()

	print("Database seeded with initial data.")