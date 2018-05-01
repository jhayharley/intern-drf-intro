from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Anime, Breed, Website
from .serializers import AnimeSerializer, BreedSerializer, WebsiteSerializer

class AnimeViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def list(self, request):
      queryset = Anime.objects.all()
      serializer = AnimeSerializer(queryset, many=True)
      return Response(serializer.data)


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