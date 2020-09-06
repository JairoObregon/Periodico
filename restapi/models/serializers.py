from rest_framework import serializers
from .models import post, category, imagenes

class PostSerializers(serializers.ModelSerializer):
        class Meta:
            model = post
            fields =  ('__all__')

class CategorySerializers(serializers.ModelSerializer):
        class Meta:
            model = category
            fields = ('__all__')

class ImagenSerializers(serializers.ModelSerializer):
        class Meta:
            model = imagenes
            fields = ('__all__')

