from rest_framework import serializers

from .models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(
		view_name='core:character-detail'
	)

	class Meta:
		model = Character
		fields = (
			'id',
			'name',
			'real_name',
			'origin',
			'gener',
			'url'
		)
