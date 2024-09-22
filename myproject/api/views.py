from rest_framework.views import APIView
from rest_framework.response import Response
from geolocations.models import Country
from .serializers import CountrySerializer
from rest_framework.decorators import api_view


class get_restapi(APIView):

    @api_view(('GET',))
    def get_data(request):
        data = {"message": "Hello, API!"}
        return Response(data)
    
    @api_view(('GET',))
    def get_country(request):
        QuerySet = Country.objects.all()
        serializer = CountrySerializer(QuerySet,many=True)
        return Response({
            "data" :serializer.data
        })