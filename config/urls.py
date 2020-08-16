from django.contrib import admin
from django.urls import path, include

api_patterns = [
	path('characters/', include('marvel.core.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/marvel/v1/', include(api_patterns)),
]
