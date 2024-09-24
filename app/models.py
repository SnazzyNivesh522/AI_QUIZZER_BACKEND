from config import db
from datetime import datetime,timezone,timedelta
ist = timezone(timedelta(hours=5, minutes=30))

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.String(50), nullable=False,unique=True)
    grade = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(ist))
    data = db.Column(db.JSON, nullable=False)
    quiz_history = db.relationship('QuizHistory', backref='quiz',lazy=True)

class QuizHistory(db.Model):
    __tablename__ = 'quiz_history'
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.String(50), nullable=False)
    # user = db.Column(db.String(50), nullable=False)
    responses = db.Column(db.JSON, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.now(ist))
    quiz_id_fk = db.Column(db.Integer, db.ForeignKey('quiz.id'))


