from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class ContactForm(db.Model):
    __tablename__ = 'contact_form'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    gender = db.Column(db.Enum('Male', 'Female'), nullable=False)
    topics = db.Column(db.String(255), nullable=False)


def start_db(app):
    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])
    with app.app_context():
        db.create_all()


def send_db(values):
    first_name, last_name, email, country, message, gender, topics_str = values

    new_entry = ContactForm(
        first_name=first_name,
        last_name=last_name,
        email=email,
        country=country,
        message=message,
        gender=gender,
        topics=topics_str
    )

    db.session.add(new_entry)
    db.session.commit()
