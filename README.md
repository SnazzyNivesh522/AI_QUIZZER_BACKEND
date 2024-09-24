# AI Quizzer API Documentation

This API provides routes to log in, generate quizzes, submit quizzes, retry quizzes, and view quiz history. Below are the details for each route along with sample request code.

---

## Authentication

### 1. Login

**Endpoint**: `/login`  
**Method**: `POST`  
**Description**: Logs in the user and returns a JWT token.

#### Request

POST /login HTTP/1.1
Host: 15.207.99.17:80
Content-Type: application/json

```json
{
    "username": "your_username",
    "password": "your_password"
}
```
#### Sample cURL Request 
```bash
curl --location --request POST "http://15.207.99.17:80/login" \
--header 'Content-Type: application/json' \
--data-raw "{
    'username': 'your_username',
    'password': 'your_password'
}"
```

GET /generate_quiz HTTP/1.1
Host: 15.207.99.17:80
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json

## QUiz ROutes

### 2. Generate Quiz
**Endpoint**: /generate_quiz
**Method**: GET
***Description**: Generates a quiz based on the given parameters. Requires JWT token.

#### Request
```json
{
    "grade": "10",
    "subject": "Math",
    "totalQuestions": 10,
    "maxScore": 100,
    "difficulty": "medium"
}
```
#### Sample cURL Request 
```bash
curl --location --request GET 'http://15.207.99.17:80/generate_quiz' \
--header 'Authorization: Bearer <YOUR_JWT_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "grade": "10",
    "subject": "Math",
    "totalQuestions": 10,
    "maxScore": 100,
    "difficulty": "medium"
}'
```

### 3. Submit Quiz 
**Endpoint** : `/submit_quiz`
**Method** : `POST`
**Description** : Submits the quiz and calculates the score based on responses. Requires JWT token.
#### Request 


```json
POST /submit_quiz HTTP/1.1
Host: 15.207.99.17:80
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json

{
    "quizId": "quiz_123456789",
    "responses": [
        {
            "questionId": "1",
            "userResponse": "B"
        },
        {
            "questionId": "2",
            "userResponse": "A"
        }
    ]
}
```

#### Sample cURL Request 


```bash
curl --location --request POST 'http://15.207.99.17:80/submit_quiz' \
--header 'Authorization: Bearer <YOUR_JWT_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "quizId": "quiz_123456789",
    "responses": [
        {
            "questionId": "1",
            "userResponse": "B"
        },
        {
            "questionId": "2",
            "userResponse": "A"
        }
    ]
}'
```
### 4. Retry Quiz 
**Endpoint** : `/retry_quiz`
**Method** : `POST`
**Description** : Allows retrying of a previously submitted quiz. Requires JWT token.
#### Request 


```json
POST /retry_quiz HTTP/1.1
Host: 15.207.99.17:80
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json

{
    "quizId": "quiz_123456789",
    "responses": [
        {
            "questionId": "1",
            "userResponse": "C"
        },
        {
            "questionId": "2",
            "userResponse": "B"
        }
    ]
}
```

#### Sample cURL Request 


```bash
curl --location --request POST 'http://15.207.99.17:80/retry_quiz' \
--header 'Authorization: Bearer <YOUR_JWT_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "quizId": "quiz_123456789",
    "responses": [
        {
            "questionId": "1",
            "userResponse": "C"
        },
        {
            "questionId": "2",
            "userResponse": "B"
        }
    ]
}'
```

### 5. Quiz History 
**Endpoint** : `/quiz_history`
**Method** : `GET`
**Description** : Retrieves the quiz history based on filters like grade, subject, and score range. Requires JWT token.
#### Request 


```json
GET /quiz_history HTTP/1.1
Host: 15.207.99.17:80
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json

[
    {
        "grade": "10",
        "subject": "Math",
        "min_score": 50,
        "max_score": 100,
        "from": "01/01/2023",
        "to": "31/12/2023"
    }
]
```

#### Sample cURL Request 


```bash
curl --location --request GET 'http://15.207.99.17:80/quiz_history' \
--header 'Authorization: Bearer <YOUR_JWT_TOKEN>' \
--header 'Content-Type: application/json' \
--data-raw '[
    {
        "grade": "10",
        "subject": "Math",
        "min_score": 50,
        "max_score": 100,
        "from": "01/01/2023",
        "to": "31/12/2023"
    }
]'
```

## Authorization Header 

For all routes that require authentication, include the following header:


```text
Authorization: Bearer <YOUR_JWT_TOKEN>
```
Replace `<YOUR_JWT_TOKEN>` with the actual token obtained from the `/login` route.

---


### Conclusion 

This API allows users to log in, generate quizzes, submit responses, retry quizzes, and retrieve quiz history. Make sure to use the JWT token obtained after logging in for authorized access.