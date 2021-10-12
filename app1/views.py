from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserInfo

# Create your views here.
@api_view(['GET'])
def helloApi(request):
    return Response("hello api") 

#회원가입 API
@api_view(['POST'])
def signInApi(request):
    a =  UserInfo()
    a.name = request.POST['name']
    a.pw = request.POST['pw']
    a.save()
    return Response("signIn Api")
