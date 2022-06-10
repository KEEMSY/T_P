from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from fast_test.serializer import TeamModelSerializer
from fast_test.models import TeamModel


class TeamView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        print('hello')
        team_list = TeamModel.objects.all()
        serializer = TeamModelSerializer(team_list, many=True)
        return JsonResponse(serializer.data,  safe=False)

    def post(self, request):
        data = {
            'result': 'success'
        }

        serializer = TeamModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(data, status=201)
        data['result'] = 'fail'
        return JsonResponse(data, status=400)

