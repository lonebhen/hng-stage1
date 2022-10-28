from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


data = {
        "slackUsername":"ben_kubi",
        "backend":True,
        "age":20,
        "bio":"I am ben, a computer engineering student aspiring to be a software engineer"

    }



def get_user_info(request):  
    if request.method == 'GET':
        response =  JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET,OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-with,Content-Type"

        return response

    




