from django.urls import path
from .views import expression_view

app_name = 'expressions'
urlpatterns = [
    path('', expression_view, name='expression'),
]