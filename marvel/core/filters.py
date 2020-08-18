from django_filters import rest_framework as filters

from .models import Character


class CharacterFilter(filters.FilterSet):
	class Meta:
		model = Character
		fields = ('gener',)
