from factory.django import DjangoModelFactory

from .models import Character


class CharacterFactory(DjangoModelFactory):
	class Meta:
		model = Character

	name = 'Spider Man'
	real_name = 'Peter Parker'
	origin = 'Lo pico una araña'
	gener = 'h'
