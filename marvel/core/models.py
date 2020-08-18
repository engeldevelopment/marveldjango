from django.db import models
from django.urls import reverse


class Character(models.Model):
	GENERS = (
		('h', 'Heroes'),
		('v', 'Villians')
	)
	name = models.CharField(max_length=80)
	real_name = models.CharField(max_length=30)
	origin = models.TextField(max_length=255)
	gener = models.CharField(max_length=2, choices=GENERS)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse(
			'core:character-detail',
			kwargs={'pk': self.pk}
		)
