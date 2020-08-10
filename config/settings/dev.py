from .base import *


DEBUG = True

CORS_ORIGIN_WHITELIST = [
	'http://localhost:4200',  # Angular
	'http://localhost:8080',  # Vue
	'http://localhost:3000',  # React
]

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('marvel/marveldb.sqlite3'),
    }
}