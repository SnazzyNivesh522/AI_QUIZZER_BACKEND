from flask import request, jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime

from sqlalchemy import and_
from config import app
from models import db,Quiz,QuizHistory

import json

from quiz_model import quiz_generator


@app.route('/generate_quiz', methods=['GET'])
@jwt_required()
def generate_quiz():
    quiz=request.get_json()
    quiz_id =f"quiz_{datetime.now().timestamp()}"
    quiz=json.loads(quiz_generator(grade=quiz['grade'],subject=quiz['subject'],total_questions=quiz['totalQuestions'],max_score=quiz['maxScore'],difficulty=quiz['difficulty']))
    new_quiz = Quiz(quiz_id=quiz_id, grade=quiz['grade'], subject=quiz['subject'], total_questions=quiz['totalQuestions'], max_score=quiz['maxScore'], difficulty=quiz['difficulty'], data=quiz['questions'])
    db.session.add(new_quiz)
    db.session.commit()
    quiz['quizId']=quiz_id
    for question in quiz["questions"]:
    	question.pop("correctAnswer", None)
    return jsonify(quiz),200

@app.route('/submit_quiz', methods=['POST'])
@jwt_required()
def submit_quiz():
    submission = request.get_json()
    quiz_id = submission['quizId']
    responses = submission['responses']

    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
    if not quiz:
        return jsonify({'message': 'Quiz not found!'}), 404
    questions = quiz.data
    score = 0
    for response in responses:
      question_id = response['questionId']
      user_answer = response['userResponse']
      for q in questions:
        if q['questionId'] == question_id and q['correctAnswer'] == user_answer:
          score += 1
    new_quiz_history = QuizHistory(quiz_id=quiz_id, responses=responses, score=score,quiz_id_fk=quiz.id)
    db.session.add(new_quiz_history)
    db.session.commit()
    return jsonify({'message': 'Quiz submitted successfully!',"score":score}),200

@app.route('/retry_quiz', methods=['POST'])
@jwt_required()
def handle_retry_quiz():
    submitted_quiz = request.get_json()
    quiz_id = submitted_quiz['quizId']
    responses = submitted_quiz['responses']
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
    if not quiz:
        return jsonify({'message': 'Quiz not found!'}), 404
    
    questions = quiz.data
    score=0
    for response in responses:
      question_id = response['questionId']
      user_answer = response['userResponse']
      for q in questions:
        if q['questionId'] == question_id and q['correctAnswer'] == user_answer:
          score += 1
    quiz_history = QuizHistory(quiz_id=quiz_id, responses=responses, score=score,quiz_id_fk=quiz.id)
    db.session.add(quiz_history)
    db.session.commit()
    return jsonify({'message': 'Quiz submitted successfully!', 'quizId': quiz.quiz_id, "score":score}),200

@app.route('/quiz_history', methods=['GET'])
@jwt_required()
def quiz_history():
    queries = request.get_json()[0]
    print(request.get_json())

    # Use get() to avoid KeyError in case the key is missing
    grade = queries.get('grade', None)
    print(f"Grade: {grade}")
    
    subject = queries.get('subject', None)
    print(f"Subject: {subject}")
    
    min_score = queries.get('min_score', 0)  # Default to 0 if not provided
    print(f"Min Score: {min_score}")
    
    max_score = queries.get('max_score', None)
    print(f"Max Score: {max_score}")
    
    start_date_str = queries.get('from', None)  # Default to None if not provided
    print(f"Start Date: {start_date_str}")
    
    end_date_str = queries.get('to', None)  # Default to None if not provided
    print(f"End Date: {end_date_str}")

    # Handle date conversion if provided
    start_date = datetime.strptime(start_date_str, '%d/%m/%Y') if start_date_str else None
    end_date = datetime.strptime(end_date_str, '%d/%m/%Y') if end_date_str else None

    # Construct query
    query = db.session.query(Quiz, QuizHistory).join(QuizHistory, Quiz.id == QuizHistory.quiz_id_fk)

    # Apply filters only if values are provided
    if grade:
        query = query.filter(Quiz.grade == grade)
    if subject:
        query = query.filter(Quiz.subject == subject)
    if min_score is not None:
        query = query.filter(QuizHistory.score >= min_score)
    if max_score is not None:
        query = query.filter(QuizHistory.score <= max_score)
    if start_date and end_date:
        query = query.filter(and_(
            QuizHistory.completed_at >= start_date,
            QuizHistory.completed_at <= end_date
        ))

    # Execute query
    quiz_data = query.all()
    print(f"Quiz Data: {quiz_data}")

    # Prepare response data
    results = []
    for quiz, history in quiz_data:
        results.append({
            'quiz_id': quiz.quiz_id,
            'grade': quiz.grade,
            'subject': quiz.subject,
            'total_questions': quiz.total_questions,
            'max_score': quiz.max_score,
            'score': history.score,
            'completed_at': history.completed_at.strftime('%d/%m/%Y'),
            'responses': history.responses
        })

    return jsonify({
        'message': 'Quiz history retrieved successfully',
        'data': results
    }), 200

if __name__ == '__main__':
  app.run(debug=True)
