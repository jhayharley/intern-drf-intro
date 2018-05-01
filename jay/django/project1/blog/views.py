from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Anime, Breed, Website
from .serializers import AnimeSerializer, BreedSerializer, WebsiteSerializer

class AnimeViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anime.objects.all().order_by('release_date')
    serializer_class = AnimeSerializer


class BreedViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class WebsiteViewSet(viewsets.ViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer