import requests
from loguru import logger

from questions.models import Questions


def get_questions(q_num: int) -> list:
    logger.info(f'Getting {q_num} questions from jservice.io')
    questions = requests.get(f"https://jservice.io/api/random?count={q_num}").json()
    if not check_questions(questions):
        logger.info('Check_questions failed, getting questions again')
        return get_questions(q_num)
    return questions


def check_questions(questions_from_jservice: list) -> bool:
    queryset = Questions.objects.all()
    for question in questions_from_jservice:
        if queryset.filter(jservice_id=question.get('id')).exists():
            logger.info('Question already exists')
            return False
    logger.info('None of the questions exists')
    return True


def get_questions_for_db(questions_from_jservice: list) -> list:
    logger.info('Prepearing questions for db')
    questions_for_db = []
    for question in questions_from_jservice:
        questions_for_db.append({
            'jservice_id': question.get('id'),
            'answer': question.get('answer'),
            'question': question.get('question'),
            'jservice_created_at': question.get('created_at'),
        })
    return questions_for_db


def save_questions(questions_for_db: list) -> None:
    for question in questions_for_db:
        Questions(**question).save()
    logger.info('Questions saved')
