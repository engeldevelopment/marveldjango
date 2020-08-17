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

		self.assertEqual(1, response.data['count'])

	def test_if_i_not_create_a_character_the_list_should_be_empty(self):

		response = self.client.get(self.url)

		self.assertEqual(0, response.data['count'])

	def test_get_all_characters_by_gener(self):

		CharacterFactory.create(
			name="Hulk",
			real_name="Brust Banner",
			gener='h',
			origin='Se expuso a rayos gammas'
		)
		self.url = '/api/marvel/v1/characters/?gener=h'

		response = self.client.get(self.url)

		self.assertEqual(1, response.data['count'])


class CharacterDetailAPIVIewTest(APITestCase):

	def test_i_can_to_see_detail_of_character(self):

		hulk = CharacterFactory.create(
			name="Hulk",
			real_name="Brust Banner",
			gener='h',
			origin='Se expuso a rayos gammas'
		)

		response = self.client.get(hulk.get_absolute_url())

		self.assertTrue(status.is_success(response.status_code))

	def test_if_not_exists_the_character_should_give_a_404(self):

		url = reverse('core:character-detail', kwargs={'pk': 2})

		response = self.client.get(url)

		self.assertTrue(status.is_client_error(response.status_code))
