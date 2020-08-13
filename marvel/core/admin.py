from django.contrib import admin

from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
	display_list = ('id', 'name', 'real_name')
