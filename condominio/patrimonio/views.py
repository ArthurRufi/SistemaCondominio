from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ConsultarPatrimonio(APIView):
    def asda(request):
        return Response(status=status.HTTP_404_NOT_FOUND)