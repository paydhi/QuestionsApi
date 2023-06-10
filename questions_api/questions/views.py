from rest_framework.response import Response
from rest_framework.views import APIView

from questions.models import Questions
from questions.serializers import QuestionsSerializer, QuestionsPostSerializer
from questions.utils import get_questions, save_questions


class QuestionsViewSet(APIView):
    serializer_class = QuestionsSerializer

    def post(self, request, *args, **kwargs):
        serializer_in_data = QuestionsPostSerializer(data=request.data)
        serializer_in_data.is_valid(raise_exception=True)

        latest_record = Questions.objects.order_by('created_at').last()
        questions_num = serializer_in_data.validated_data.get('questions_num')

        questions = get_questions(questions_num)
        save_questions(questions)

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
