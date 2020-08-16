from django.test import SimpleTestCase
from django.urls import resolve

from ..views import CharacterListAPIView, CharacterDetailAPIView


class EndPointsOfCoreAppTest(SimpleTestCase):

	def test_list_of_characters(self):

		url = '/api/marvel/v1/characters/'

		self.assertEqual(CharacterListAPIView, resolve(url).func.view_class)

	def test_detail_of_character(self):

		url = '/api/marvel/v1/characters/1'

		self.assertEqual(CharacterDetailAPIView, resolve(url).func.view_class)
