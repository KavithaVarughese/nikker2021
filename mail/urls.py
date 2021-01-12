from django.urls import path
from .views import mail_view

app_name = 'mail'
urlpatterns = [
    path('', mail_view, name='mail'),
]