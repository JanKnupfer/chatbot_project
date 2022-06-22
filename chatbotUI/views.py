from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Question
from .serializer import QuestionSerializer


def index(request):
    return render(request, 'chat/index.html')


class QuestionApiView(APIView):
    serializer_class = QuestionSerializer

    # add permission to check if user is authenticated

    # 1. List all
    # def get(self, request, *args, **kwargs):
    #     '''
    #     List all the to-do items for given requested user
    #     '''
    #     question = Question.objects.filter()
    #     serializer = TodoSerializer(question, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the To-do with given to-do data
        '''
        question_data = request.data
        data = {
            'question': question_data.get('question')
        }
        serializer = QuestionSerializer(data=question_data)
        if serializer.is_valid():
            return Response(data={"answer": "42"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetailApiView(APIView):
    # add permission to check if user is authenticated

    def get_object(self):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Question.objects.get()
        except Question.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        question_instance = self.get_object()
        if not question_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = QuestionSerializer(question_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
