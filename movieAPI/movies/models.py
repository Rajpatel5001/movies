#from files
from .choese import gender,cast,stat,film_certificate

#from core Djnago
from django.db import models

class basicinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True 

class Imagesmodel(basicinfo):
    img = models.ImageField(upload_to='', null=True, max_length=255)
    

class PersonModel(basicinfo):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)

class genresmodel(basicinfo):
    genre = models.CharField(max_length=50,unique=True)

class MoviesModel(basicinfo):

    #user_input fields

        #string
    name = models.CharField(max_length=100,unique=True)
    storyline = models.TextField()
        #integer
    rating = models.DecimalField(decimal_places=2,max_digits=4)
    cost = models.PositiveIntegerField()
    profit = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
        #Datetimeinput(YYYY-MM-DD)
    date = models.DateField()

    #choiese fields
    film_certificate = models.CharField(max_length=20,choices=film_certificate)
    cast_on = models.CharField(max_length=50,choices=cast)

    #multichoese fields
    genres = models.ManyToManyField(genresmodel,related_name="moviegenres")
    teammates = models.ManyToManyField(PersonModel,related_name="movieteammates")
    # img = models.ManyToManyField(Imagesmodel,related_name="movieimage")

    #imagefileds
    img = models.ImageField(upload_to='', max_length=255)

class NotesModel(basicinfo):
    notes = models.TextField()
    movie  = models.ForeignKey(MoviesModel,on_delete=models.CASCADE,related_name="comments")

class songModel(basicinfo):
    songname = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    relased_data = models.DateField()
    movie = models.ForeignKey(MoviesModel,on_delete=models.CASCADE,related_name="song")

class actorModel(basicinfo):
    #input
        #str
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)

        #date
    born = models.DateField()

        #integer
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()

        #choices
    gender = models.CharField(max_length=20,choices=gender)
    status = models.CharField(max_length=20,choices=stat)
    Awards = models.CharField(max_length=200)
    familybackground = models.TextField()
    otheroccupation = models.CharField(max_length=100)
    biodata = models.TextField()

        #forenkey - many to many
    movies = models.ManyToManyField(MoviesModel,related_name= "movieactor")
