from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from questions.models import Questions
from questions.serializers import QuestionsSerializer


class QuestionsViewSet(APIView):
    def post(self, request):
        if not request.data.get('questions_num'):
            content = {'detail': 'questions_num is required'}
            return Response(content, status=400)
        elif not isinstance(request.data.get('questions_num'), int):
            content = {'detail': 'questions_num must be integer'}
            return Response(content, status=400)
        elif request.data.get('questions_num') < 1:
            content = {'detail': 'questions_num must be greater than 0'}
            return Response(content, status=400)
        else:
            try:
                latest_record = Questions.objects.latest('id')
            except Questions.DoesNotExist:
                latest_record = {}
            fin = False
            while not fin:
                questions = requests.get(f"https://jservice.io/api/random?count={request.data.get('questions_num')}")
                questions = questions.json()
                i = 0
                for question in questions:
                    if Questions.objects.filter(jservice_id=question['id']).exists():
                        break
                    question_for_db = {
                        'jservice_id': question['id'],
                        'answer': question['answer'],
                        'question': question['question'],
                        'jservice_created_at': question['created_at'],
                    }
                    question_for_db = Questions(**question_for_db)
                    question_for_db.save()
                    i += 1
                if i == len(questions):
                    fin = True
        if latest_record != {}:
            return Response(QuestionsSerializer(latest_record, many=False).data, status=200)
        elif latest_record == {}:
            return Response(latest_record, status=400)
        else:
            return Response({'detail': 'No questions found on jservice.io'}, status=400)

    def options(self, request, *args, **kwargs):
        options_data = {
            'expect': {
                'methods': {
                    'OPTIONS': None,
                    'POST': {
                        'method': 'POST',
                        'JSON': {'questions_num': 'int', },
                    },
                },
                'return': {
                    'id': 'int: id_in_db',
                    'jservice_id': 'int: id in jservice.io db',
                    'answer': 'str: answer to question',
                    'question': 'str: random question from jservice.io',
                    'jservice_created_at': 'datetime: date at which question was created in jservice.io db',
                },
            },
        }
        return Response(options_data, status=200)
