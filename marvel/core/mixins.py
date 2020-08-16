from .models import Character
from .serializers import CharacterSerializer


class CharacterMixinAPIView(object):
	serializer_class = CharacterSerializer
	queryset = Character.objects.all()
