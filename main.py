from fastapi import FastAPI, status

from models import Answer, Question
from schemas import CreateQuestionRequest


app = FastAPI()

questions: list[Question] = [
    Question(
        title="How do you make a for loop?",
        question="I've been trying to make a for loop, but I just can't figure it out, can anyone help?",
        topic="Python",
        likes=3,
        user="Tony",
        answers=[
            Answer(
                response="Why would you even want to do it that way?",
                likes=80,
                answered=False,
                user="Treyson",
            ),
            Answer(
                response="Git gud scrub",
                likes=6000,
                answered=False,
                user="Brandon",
            ),
            Answer(
                response="It should look something like this: for i in range(10):...",
                likes=47,
                answered=True,
                user="Hannah",
            ),
        ],
    )
]

@app.get("/questions")
async def get_questions() -> list[Question]:
    return questions

@app.post("/questions", status_code=status.HTTP_201_CREATED)
async def create_question(create_question_request: CreateQuestionRequest) -> Question:
    question: Question = Question(**create_question_request.model_dump())
    questions.append(question)
    return question