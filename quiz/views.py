from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerialzer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("Hello World!")