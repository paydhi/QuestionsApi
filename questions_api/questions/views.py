from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from questions.models import Question


class QuestionsViewSet(APIView):
    def post(self, request):
        if not request.data.get('questions_num'):
            return Response.status_code(400)
        elif not isinstance(request.data.get('questions_num'), int):
            return Response.status_code(400)
        else:
            fin = False
            while not fin:
                questions = requests.get(f"https://jservice.io/api/random?count={request.data.get('questions_num')}")
                questions = questions.json()
                i = 0
                for question in questions:
                    if Question.objects.filter(jservice_id=question['id']).exists():
                        break
                    question_for_db = {
                        'jservice_id': question['id'],
                        'answer': question['answer'],
                        'question': question['question'],
                        'question_created_at': question['created_at'],
                    }
                    question_for_db = Question(**question_for_db)
                    question_for_db.save()
                    i += 1
                if i == len(questions):
                    fin = True
        if questions:
            return Response(questions)
        else:
            return Response.status_code(400)


def options(self, request, *args, **kwargs):
    return Response({'message': 'Success',
                     'expect': {'questions_num': 'int'},
                     'return': {
                         'message': 'Success',
                         'questions_num': 'int'}})
