#from djnago core
import json

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

#rest_framwork
from rest_framework.views import APIView 
from rest_framework.response import Response

#from files
from .serilizer import Movieserilizer,Noteserilizer,Actorserilizer,songserilizer,Imagesmodel,Imageserilizer
from .models import MoviesModel,NotesModel,actorModel,songModel

class movieview(APIView):
    def get(self,request,*args,**kwargs):
        objs = MoviesModel.objects.all()
        if 'pk' in kwargs:
            objs = objs.filter(id = self.kwargs['pk'])
            id = self.kwargs['pk']
        serilized = Movieserilizer(objs,many=True)
        return Response({
            "message":serilized.data
        })
    
    def post(self,request):
        serilizedata = Movieserilizer(data=request.data)
        if serilizedata.is_valid():
            serilizedata.save()
            message = EmailMultiAlternatives(subject='Applicant data', from_email=settings.EMAIL_HOST_USER,to=('backend3.techwe@gmail.com',))
            message.attach_file( serilizedata.data['img'][10:])
            message.attach_alternative(json.dumps(serilizedata.data,indent = 4) , mimetype='application/json')
            message.send()
            return Response({
                "messga":serilizedata.data
            })
        else:
            return Response({
                "message":serilizedata.errors
            })    

class NotesVies(APIView):
    def get(self,request,pk=None):
        if pk is None:
            objs = NotesModel.objects.all()
        else:
            objs = NotesModel.objects.filter(movie_id = pk).all()
        serilized = Noteserilizer(objs,many=True)
        return Response({
            "message":serilized.data
        })
    def post(self,request,pk=None):
        serilizedata = Noteserilizer(data=request.data,context={"pk":self.kwargs['pk']})
        if serilizedata.is_valid():
            serilizedata.save()
            return Response({
                "messga":serilizedata.data
            })
        else:
            return Response({
                "message":serilizedata.errors
            })    
        
class ActorVies(APIView):
    def get(self,request,pk=None):
        if pk is None:
            objs = actorModel.objects.all()
        else:
            objs = actorModel.objects.filter(id = pk).all()
        serilized = Actorserilizer(objs,many=True)
        return Response({
            "message":serilized.data
        })
    
    def post(self,request):
        serilizedata = Actorserilizer(data=request.data)
        if serilizedata.is_valid():
            serilizedata.save()
            return Response({
                "messga":serilizedata.data
            })
        else:
            return Response({
                "message":serilizedata.errors
            })   
        
class SongsVies(APIView):
    def get(self,request,pk=None):
        if pk is None:
            objs = songModel.objects.all()
        else:
            objs = songModel.objects.filter(movie_id = pk).all()
        serilized = songserilizer(objs,many=True)
        return Response({
            "message":serilized.data
        })
    def post(self,request,pk=None):
        serilizedata = songserilizer(data=request.data,context={"pk":self.kwargs['pk']})
        if serilizedata.is_valid():
            serilizedata.save()
            return Response({
                "messga":serilizedata.data
            })
        else:
            return Response({
                "message":serilizedata.errors
            }) 
           
class ImageView(APIView):
    def get(self,request,pk=None):
        if pk is None:
            objs = Imagesmodel.objects.all()
        else:
            objs = Imagesmodel.objects.filter(id = pk).all()
        serilized = Imageserilizer(objs,many=True)
        return Response({
            "message":serilized.data
        })
    def post(self,request,pk=None):
        serilizedata = Imageserilizer(data=request.data,context={"pk":self.kwargs['pk']})
        if serilizedata.is_valid():
            serilizedata.save()
            return Response({
                "messga":serilizedata.data
            })
        else:
            return Response({
                "message":serilizedata.errors
            })    
