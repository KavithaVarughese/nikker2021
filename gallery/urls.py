from django.urls import path
from .views import collage_view

app_name = 'gallery'
urlpatterns = [
    path('', collage_view, name='collage'),
]