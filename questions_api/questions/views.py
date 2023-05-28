from rest_framework.views import APIView
from rest_framework.response import Response

from questions.models import Questions
from questions.serializers import QuestionsSerializer
from questions.utils import get_questions, get_questions_for_db, save_questions


class QuestionsViewSet(APIView):
    def post(self, request):
        latest_record = Questions.objects.last()
        questions_num = request.data.get('questions_num')

        questions = get_questions(questions_num)
        questions_for_db = get_questions_for_db(questions)
        save_questions(questions_for_db)

        if latest_record:
            return Response(QuestionsSerializer(latest_record, many=False).data, status=200)
        else:
            return Response({}, status=200)


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
