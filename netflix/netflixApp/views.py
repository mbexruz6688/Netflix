from rest_framework import generics, serializers
from .serializer import *
from .models import *
from rest_framework.filters import OrderingFilter, SearchFilter

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends =[SearchFilter, OrderingFilter, ]
    search_fields = ['name', 'genre',]
    ordering_fields = ['imdb',]


class aMovie(generics.RetrieveAPIView):
    queryset =Movie.objects.all()
    serializer_class = MovieSerializer

class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends =[SearchFilter, OrderingFilter, ]
    search_fields = ['name',]
    ordering_fields = ['birth_date', ] 