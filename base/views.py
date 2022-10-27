from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def get_user_info(request):
    data = {
        "slackUsername":"ben kubi",
        "backend":True,
        "age":20,
        "bio":"I am ben, a computer engineering student aspiring to be a software engineer"

    }
    error = {
        "message":"Invalid request method"
    }
    if request.method == 'GET':
        return JsonResponse(data)

    return JsonResponse(error)




