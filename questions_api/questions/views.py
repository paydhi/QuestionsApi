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
            questions = requests.get(f"https://jservice.io/api/random?count={request.data.get('questions_num')}")
            questions = questions.json()
            for question in questions:
                question_for_db = {
                        'jservice_id': question['id'],
                        'answer': question['answer'],
                        'question': question['question'],
                        'question_created_at': question['created_at'],
                    }
                question_for_db = Question(**question_for_db)
                question_for_db.save()
            return Response(questions)


    def options(self, request, *args, **kwargs):
        return Response({'message': 'Success',
                         'expect': {'questions_num': 'int'},
                         'return': {
                             'message': 'Success',
                             'questions_num': 'int'}})
