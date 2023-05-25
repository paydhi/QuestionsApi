from rest_framework.views import APIView
from rest_framework.response import Response


class QuestionsViewSet(APIView):
    def post(self, request):
        questions_num = request.data.get('questions_num')
        return Response({'message': 'Success', 'questions_num': questions_num})

    def options(self, request, *args, **kwargs):
        return Response({'message': 'Success',
                         'expect': {'questions_num': 'int'},
                         'return': {
                             'message': 'Success',
                             'questions_num': 'int'}})
