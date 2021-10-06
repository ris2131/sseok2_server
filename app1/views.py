from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserInfo

# Create your views here.
@api_view(['GET'])
def helloApi(request):
    return Response("hello api") 