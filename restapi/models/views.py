from django.shortcuts import render
from rest_framework import viewsets
#models
from .models import post, category, imagenes
#serializer_class
from .serializers import PostSerializers, CategorySerializers, ImagenSerializers

# Create your views here.

class categoryView(viewsets.ModelViewSet):
    queryset = category.objects.all()
    serializer_class = CategorySerializers

class postView(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializers

class postcategoryView(viewsets.ModelViewSet):
    serializer_class = PostSerializers

    def get_queryset(self):
        id = self.kwargs['username']
        print(post.objects.filter(category__nombreCategoria=id))
        return post.objects.filter(category__nombreCategoria=id)

class imagenesView(viewsets.ModelViewSet):
    queryset = imagenes.objects.all()
    serializer_class = ImagenSerializers

class portadaView(viewsets.ModelViewSet):
    serializer_class = PostSerializers

    def get_queryset(self):
        i = 0
        data = [] 
        a = post.objects.filter(category__nombreCategoria="portada")
        while i<3:
            print(a[i])
            data.append(a[i])
            i=i+1
        
        print(data)
        return data

class politicaView(viewsets.ModelViewSet):
    serializer_class = PostSerializers

    def get_queryset(self):
        i = 0
        data = [] 
        a = post.objects.filter(category__nombreCategoria="politica")
        while i<3:
            print(a[i])
            data.append(a[i])
            i=i+1
        
        print(data)
        return data

class policialView(viewsets.ModelViewSet):

    serializer_class = PostSerializers

    def get_queryset(self):
        i = 0
        data = [] 
        a = post.objects.filter(category__nombreCategoria="policial")
        while i<3:
            print(a[i])
            data.append(a[i])
            i=i+1
        
        print(data)
        return data

class deportesView(viewsets.ModelViewSet):
    serializer_class = PostSerializers

    def get_queryset(self):
        i = 0
        data = [] 
        a = post.objects.filter(category__nombreCategoria="deportes")
        while i<5:
            print(a[i])
            data.append(a[i])
            i=i+1
        
        print(data)
        return data

class entretenimientoView(viewsets.ModelViewSet):
    serializer_class = PostSerializers

    def get_queryset(self):
        i = 0
        data = [] 
        a = post.objects.filter(category__nombreCategoria="entretenimiento")
        while i<3:
            print(a[i])
            data.append(a[i])
            i=i+1
        
        print(data)
        return data

class viajesView(viewsets.ModelViewSet):
    serializer_class = PostSerializers

    def get_queryset(self):
        i = 0
        data = [] 
        a = post.objects.filter(category__nombreCategoria="viajes")
        while i<3:
            print(a[i])
            data.append(a[i])
            i=i+1
        
        print(data)
        return data