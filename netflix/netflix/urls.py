from django.contrib import admin
from django.urls import path
from netflixApp.views import ActorCreateListView

from netflixApp.serializer import MovieSerializer
from netflixApp.views import MovieList, aMovie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', MovieList.as_view()),
    path('actor/', ActorCreateListView.as_view()),
    path('movie/<int:pk>', aMovie.as_view()),
]