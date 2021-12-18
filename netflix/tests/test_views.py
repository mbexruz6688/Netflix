from django.test import TestCase
from django.test.client import Client
from netflixApp.models import *
from netflixApp.serializer import *


class TestMovieList(TestCase):
    def setUp(self) -> None:
        self.cl = Client()

    def test_all_movies(self):
        movies = self.cl.get("/movie/").data
        self.assertEqual(len(movies), 0)
        assert len(movies) == 0

    def test_post_an_actor(self):
        movie = {
            "id" : 1,
            "name":"Ulug'bek Qodirov",
            "birth_date":"1985-10-23",
            "gender":"Male"
        }
        mov2 = {
            "id" : 1,
            "name":"Tom Hardin",
            "birth_date":"1985-5-3",
            "gender":"Male"
        }
        a = self.cl.post("/actor/", data=movie)
        b = self.cl.post("/actor/", data=mov2)
        assert a.status_code == 201
        actors = self.cl.get("/actor/").data
        assert actors is not None
        # assert actors[0]['name'] == "Ulug'bek Qodirov"
        # assert actors[0]['gender'] == "Male"
        # assert actors[0]['birth_date'] == "1985-10-23"

class TestActorCreateList(TestCase):
    def setUp(self) -> None:
        self.cl = Client()

    def test_post_an_actor(self):
        aktyor = {
            "id" : 1,
            "name":"Ulug'bek Qodirov",
            "birth_date":"1985-10-23",
            "gender":"Male"
        }
        ak2 = {
            "id" : 1,
            "name":"Tom Hardin",
            "birth_date":"1985-5-3",
            "gender":"Male"
        }
        a = self.cl.post("/actor/", data=aktyor)
        b = self.cl.post("/actor/", data=ak2)
        assert a.status_code == 201
        actors = self.cl.get("/actor/").data
        assert actors is not None
        assert actors[0]['name'] == "Ulug'bek Qodirov"
        assert actors[0]['gender'] == "Male"
        assert actors[0]['birth_date'] == "1985-10-23"