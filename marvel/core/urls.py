from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
	path('', views.CharacterListAPIView.as_view(), name='characters'),
]
