import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerialzer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello World!")

@api_view(['GET'])
def randomQuiz(request, id=3):
    totalQuizs = Quiz.objects.all()
    randomQuiz = random.sample(list(totalQuizs), id)
    serializer = QuizSerialzer(randomQuiz, many=True) # many=True는 여러개의 데이터를 직렬화할 때 사용
    return Response(serializer.data)