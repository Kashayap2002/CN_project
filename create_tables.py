from app import app, db
from app import Booking  # Assuming 'Booking' is your SQLAlchemy model

def create_tables():
    with app.app_context():
        db.init_app(app)  # Initialize the app with the database instance
        db.create_all()  # Create all tables if they don't exist

if __name__ == '__main__':
    create_tables()
