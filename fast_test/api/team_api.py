from rest_framework.response import Response
from rest_framework.views import APIView
from fast_test.serializer import TeamModelSerializer
from fast_test.models import TeamModel


class TeamView(APIView):
    def get(self, request):
        team_list = TeamModel.objects.all()
        serializer = TeamModelSerializer(team_list, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = TeamModelSerializer(data=request.data)
