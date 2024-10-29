
# Trivia Program

### Video Demo: 

### Description:

This is a Python-based trivia program that provide's users with multiple-choice trivia questions using Open Trivia's API. The program prompts users to select a category, difficulty level, and number of questions, then presents them with the corresponding trivia questions. It also tracks the user’s score and updates high scores across different sessions.



### Running the program


```python

usage: python project.py

get the corresponding requested questions 

### running the test

run the test using the following command

```bash
  pytest
```
## API Reference


#### Get Trivia Questions

```http
  GET /api.php
```
| parameter   | Type    | Description                                                             |
|-------------|---------|-------------------------------------------------------------------------|
| amount      | integer | The number of questions to retrieve (5 or 10)                           |
| category    | integer | The category ID of the trivia questions (e.g., 9 for General Knowledge) |
| difficulty  | string  | The difficulty level of the questions: easy, medium, or hard            |
| type        | string  | The type of questions to retrieve. Default is multiple                  |

#### Get Item by ID

```http
  GET /api/items/${id}

| Parameter   | Type    | Description                                                                                                                 |
|-------------|---------|-----------------------------------------------------------------------------------------------------------------------------|
| id          | integer | The unique ID of the trivia question to fetch. This ID is typically assigned by the trivia API when questions are retrieved |

Example Request
http
Copy code
GET /api/items/1
Example Response
json
Copy code
{
  "category": "General Knowledge",
  "type": "multiple",
  "difficulty": "medium",
  "question": "What is the capital of Australia?",
  "correct_answer": "Canberra",
  "incorrect_answers": [
    "Sydney",
    "Melbourne",
    "Brisbane"
  ]
}

## Authors

- [@kalutm](https://www.github.com/kalutm)

