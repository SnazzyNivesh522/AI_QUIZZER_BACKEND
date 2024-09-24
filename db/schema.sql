CREATE DATABASE IF NOT EXISTS AI_QUIZ_APP;

USE AI_QUIZ_APP;

CREATE TABLE quiz (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id VARCHAR(50) NOT NULL UNIQUE,
    grade INT NOT NULL,
    subject VARCHAR(50) NOT NULL,
    total_questions INT NOT NULL,
    max_score INT NOT NULL,
    difficulty VARCHAR(10) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    data JSON NOT NULL
);

CREATE TABLE quiz_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id VARCHAR(50) NOT NULL,
    responses JSON NOT NULL,
    score INT NOT NULL,
    completed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    quiz_id_fk INT,
    FOREIGN KEY (quiz_id_fk) REFERENCES quiz(id)
);