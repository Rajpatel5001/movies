from rest_framework import serializers
from .models import MoviesModel
from .choese import ch
class Movieserilizer(serializers.ModelSerializer):
    class Meta:
        model =MoviesModel
        fields = '__all__'

