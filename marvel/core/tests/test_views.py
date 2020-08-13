from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from marvel.core.factories import CharacterFactory


class CharacterListAPIViewTest(APITestCase):

	def setUp(self):

		self.url = reverse('core:characters')

	def test_get_all_characters(self):

		CharacterFactory.create(
			name="Hulk",
			real_name="Brust Banner",
			gener='h',
			origin='Se expuso a rayos gammas'
		)

		response = self.client.get(self.url)

		self.assertEqual(status.HTTP_200_OK, response.status_code)
		self.assertEqual(1, response.data['count'])

	def test_if_i_not_create_a_character_the_list_should_be_empty(self):

		response = self.client.get(self.url)

		self.assertEqual(status.HTTP_200_OK, response.status_code)
		self.assertEqual(0, response.data['count'])
