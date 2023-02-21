from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serilizer import Movieserilizer
from rest_framework.response import Response

class movieview(APIView):
    def post(self,request):
        r_data = Movieserilizer(data=request.data)
        if r_data.is_valid():
            r_data.save()
            return Response({
                "messga":r_data.data
            })
        else:
            return Response({
                "message":r_data.errors
            })    

