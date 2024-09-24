from config import app,db
from models import Quiz,QuizHistory
with app.app_context():
    db.create_all()