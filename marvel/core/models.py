from django.db import models


class Character(models.Model):
	GENERS = (
		('h', 'Heroes'),
		('m', 'Villians')
	)
	name = models.CharField(max_length=80)
	real_name = models.CharField(max_length=30)
	origin = models.TextField(max_length=255)
	gener = models.CharField(max_length=2, choices=GENERS)

	def __str__(self):
		return self.name
