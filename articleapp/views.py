from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from articleapp.service import project_db_service


@csrf_exempt
def find_all_article(request):
    if request.method == "GET":
        result = project_db_service.find_all_article()
        return JsonResponse(result, status=201, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        project_db_service.make_article(data=data)


