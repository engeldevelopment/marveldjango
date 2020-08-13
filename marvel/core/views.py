from rest_framework import generics

from .models import Character
from .serializers import CharacterSerializer


class CharacterListAPIView(generics.ListAPIView):
	serializer_class = CharacterSerializer
	queryset = Character.objects.all()
