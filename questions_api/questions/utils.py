import requests
from loguru import logger

from questions.models import Questions


def get_questions(q_num: int) -> list:
    logger.info('Getting {} questions from jservice.io', q_num)
    questions = []
    while q_num > 0:
        new_questions = requests.get(f"https://jservice.io/api/random?count={q_num}").json()
        jservice_ids = set(question.get('id') for question in new_questions)
        existing_ids = set(Questions.objects.filter(jservice_id__in=jservice_ids).values_list('jservice_id', flat=True))
        new_questions = [question for question in new_questions if question.get('id') not in existing_ids]
        if not new_questions:
            break
        questions.extend(new_questions)
        q_num -= len(new_questions)
        if not questions:
            logger.info('Got non-unique questions, getting remaining {} questions', q_num)
            return get_questions(q_num)

    questions_to_return = [{
            'jservice_id': question.get('id'),
            'answer': question.get('answer'),
            'question': question.get('question'),
            'jservice_created_at': question.get('created_at')
        } for question in questions]
    return questions_to_return


def save_questions(questions: list) -> None:
    questions_list = [Questions(**question) for question in questions]
    Questions.objects.bulk_create(questions_list)
    logger.info('Questions saved')
