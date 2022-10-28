from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.



data = {
        "slackUsername":"ben_kubi",
        "backend":True,
        "age":20,
        "bio":"I am ben, a computer engineering student aspiring to be a software engineer"

    }
error = {
        "message":"Invalid request method"
    }


@api_view(['GET'])
def get_user_info(request):
    
    if request.method == 'GET':
        return Response(data)

    return Response(error)




