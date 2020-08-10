from .base import *


DEBUG = False

CORS_ORIGIN_WHITELIST = [
	# Agregar host permitidos para compartir información
]

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('marvel/marveldb.sqlite3'),
    }
}