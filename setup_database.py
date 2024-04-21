from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Update the password to 'pass'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pass@localhost/feedback_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

def create_database():
    """Create the database if it doesn't exist."""
    with app.app_context():
        db.create_all()

def create_tables():
    """Create tables in the database."""
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    create_database()
    create_tables()
