from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer
from drf_yasg.utils import swagger_auto_schema
import google.generativeai as genai
import os


# API KEY A METTRE ICI.
api_key = "METTRE L'API KEY ICI"

class AllTranslationViewSet(APIView):

    def get(self, request):
        result = Translation.objects.all()
        serialized_data = TranslationSerializer(result, many=True)
        return Response(data=serialized_data.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TranslationSerializer)
    def post(self, request):
        source_language = request.data.get('source_language')
        source_text = request.data.get('source_text')
        target_language = request.data.get('target_language')

        if not source_language or not source_text or not target_language:
            return Response(data={'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"Translate '{source_text}' from {source_language} to {target_language}. The response should only contain the translation."

        try:
            response = model.generate_content(prompt)
            target_text = response.text.strip()

            translation = Translation.objects.create(
                source_language=source_language,
                source_text=source_text,
                target_language=target_language,
                target_text=target_text
            )

            return Response(data={
                'TRADUCTIONS (^_^)': target_text
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class FrenchSpanishTranslationViewSet(APIView):

   
   def get(self, request):
        
        self.source_language = request.GET.get('source_language', 'Français')
        self.target_language = request.GET.get('target_language', 'Espagnol')
        self.target_text = request.GET.get('target_text', 'Espagnol')
        self.author = request.GET.get('author', 'Bakops')
        
        result = Translation.objects.all()
        serialized_data = TranslationSerializer(result, many=True)
        
        return Response(data={
            'source_language': self.source_language,
            'target_language': self.target_language,
            'author': self.author,
        }, status=status.HTTP_200_OK)
    

def post(self, request):
        source_language = ("FR")
        source_text = ("J'aime les chat")
        target_language = ("ES")
        target_text = ("I love cat ")
        
        Translation.objects.create(source_language=source_language, source_text=source_text, target_language=target_language, target_text=target_text)

        return Response(data={
            "Result": "Translation added",
            "Translation": target_text

        }, 
        status=status.HTTP_201_CREATED
        )

def put(self, request, pk):
    return Response(data={}, status=None)

def delete(self, request, pk):
    return Response(data={}, status=None)













class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        author = request.GET.get('autor','Pas d/auteur')
        result = Translation.objects.all()
        serialized_data = TranslationSerializer(result, many=True)
        return Response(data={'result', author}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)



def index(request):
    return render(request, 'index.html', context={})
