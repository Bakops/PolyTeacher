from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer


# Create your views here.
class FrenchSpanishTranslationViewSet(APIView):

   
    def get(self, request):
        result = Translation.objects.all()
        serialized_data = TranslationSerializer(result, many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        result = Translation.objects.all()
        serialized_data = TranslationSerializer(result, many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class AllTranslationViewSet(APIView):

    def get(self, request):
         autor = request.GET.get('autor','Pas d/auteur')
         result = Translation.objects.all()
         serialized_data = TranslationSerializer(result, many=True)
         return Response(data=serialized_data.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

def index(request):
    return render(request, 'index.html', context={})