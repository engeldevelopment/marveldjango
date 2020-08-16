from rest_framework import generics

from .mixins import CharacterMixinAPIView


class CharacterListAPIView(CharacterMixinAPIView, generics.ListAPIView):
	pass


class CharacterDetailAPIView(CharacterMixinAPIView, generics.RetrieveAPIView):
	pass
