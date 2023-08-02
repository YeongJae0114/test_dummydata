from django.shortcuts import render
from rest_framework import viewsets
from .serializers import serializersPost
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializersPost