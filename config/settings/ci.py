from .base import *


DEBUG = True

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('marvel/marveldb.sqlite3'),
    }
}