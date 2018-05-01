from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Anime, Breed, Website
from .serializers import AnimeSerializer, BreedSerializer, WebsiteSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anime.objects.all().order_by('-release_date')
    serializer_class = AnimeSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Breed.objects.all().order_by('-name')
    serializer_class = BreedSerializer

class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Website.objects.all().order_by('-name')
    serializer_class = WebsiteSerializer