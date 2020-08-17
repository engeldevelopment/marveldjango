from rest_framework import generics

from .filters import CharacterFilter
from .mixins import CharacterMixinAPIView


class CharacterListAPIView(CharacterMixinAPIView, generics.ListAPIView):
	filterset_class = CharacterFilter


class CharacterDetailAPIView(CharacterMixinAPIView, generics.RetrieveAPIView):
	pass
