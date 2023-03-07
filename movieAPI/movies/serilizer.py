#from rest_frmework
from rest_framework import serializers

#from djnago core files
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile

#from  file
from .models import MoviesModel , NotesModel , songModel , actorModel , genresmodel, PersonModel,Imagesmodel

#3rd party
from drf_extra_fields.fields import Base64ImageField
import base64


class genreserilizer(serializers.ModelSerializer):
    class Meta:
        model = genresmodel
        # fields = '__all__'
        exclude = ('created_at','updated_At')   
class Imageserilizer(serializers.ModelSerializer):
    imgs = Base64ImageField(source='img')
    def create(self,data):
        pk = self.context["pk"]
        try:
            movieobj = MoviesModel.objects.get(id = pk)
        except:
            raise serializers.ValidationError(_(f"no movie object at {pk}"))
        imgobj = Imagesmodel.objects.create(**data)
        imgobj.movieimage.add(movieobj)
        return imgobj


    class Meta:
        model = Imagesmodel
        exclude = ('created_at','updated_At')
class personserilizer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        exclude = ('created_at','updated_At')
class Noteserilizer(serializers.ModelSerializer):
    class Meta:
        model = NotesModel
        # fields = '__all__'
        depth = 0
        exclude = ('created_at','updated_At')

    def to_internal_value(self, data):
        return data
    def create(self,validated_data):
        pk = self.context["pk"]
        try:
            movieobj = MoviesModel.objects.get(id = pk)
        except:
            raise serializers.ValidationError(_(f"no movie object at {pk}"))
        note = NotesModel.objects.create(movie = movieobj,**validated_data)
        return note
class songserilizer(serializers.ModelSerializer):
    class Meta:
        model = songModel
        # fields = '__all__'
        depth =0
        exclude = ('created_at','updated_At')

    def to_internal_value(self, data):
        return data
    def create(self,validated_data):
            pk = self.context["pk"]
            try:
                movieobj = MoviesModel.objects.get(id = pk)
            except:
                raise serializers.ValidationError(_(f"no movie object at {pk}"))
            
            song = songModel.objects.create(movie = movieobj,**validated_data)
            return song
class Actorserilizer(serializers.ModelSerializer):
    topmovies = serializers.SerializerMethodField()

    def get_topmovies(self,obj):
        return "1"
    class Meta:
        model = actorModel
        # fields = '__all__'
        exclude = ('created_at','updated_At')
class Actormainsrilizer(Actorserilizer):
    class Meta:
        depth = 2
class Movieserilizer(serializers.ModelSerializer):
    comment = Noteserilizer(many=True,source='comments')
    songs = songserilizer(many=True,source='song')
    actor = Actorserilizer(many=True,source='movieactor')
    genres = genreserilizer(many=True)
    team = personserilizer(many=True,source='teammates')
    bestmovie = serializers.SerializerMethodField()
    blogbuster = serializers.SerializerMethodField()

    def get_bestmovie(self,obj):
        return MoviesModel.objects.all().order_by('-rating').first().name

    def get_blogbuster(self,obj):
        if obj.profit>1000000:
            return True
        else:
            return False

    def to_internal_value(self, data):
        format, imgstr = data['img'].split(';base64,') 
        ext = format.split('/')[-1] 
        data['img'] = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return data
    
    def create(self, validated_data):
        comments = validated_data.pop('comment')
        songs = validated_data.pop('song')
        actors = validated_data.pop('actor')
        genres = validated_data.pop('genres')
        teammatess  = validated_data.pop('teammate')  
        try:
            movieobj = MoviesModel.objects.get(**validated_data)
        except:
            movieobj = MoviesModel.objects.create(**validated_data)
        for comment in comments:
            try:
                com = NotesModel.objects.filter(movie=movieobj,**comment).get()
            except:
                com = NotesModel.objects.create(movie=movieobj,**comment)
        for song in songs:
            try:
                com = songModel.objects.filter(movie=movieobj,**song).get()
            except ObjectDoesNotExist:
                com = songModel.objects.create(movie=movieobj,**song)
        for actor in actors:
            try:
                com = actorModel.objects.filter(**actor).get()
            except:
                com = actorModel.objects.create(**actor)
            try:
                movieobj.movieactor.get(com)
            except:
                movieobj.movieactor.add(com)
        for genre in genres:
            try:
                com = genresmodel.objects.filter(**genre).get()
            except:
                com = genresmodel.objects.create(**genre)
            try:
                com.moviegenres.get(movieobj)
            except:
                com.moviegenres.add(movieobj)
        for teammate in teammatess:
            try:
                com = PersonModel.objects.filter(**teammate).get()
            except:
                com = PersonModel.objects.create(**teammate)
            try:
                com.movieteammates.get(movieobj)
            except:
                com.movieteammates.add(movieobj)
        return movieobj
    
    class Meta:
        model =MoviesModel
        # fields = '__all__'
        exclude = ('created_at','updated_At')