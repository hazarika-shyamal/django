from django.urls import path
from .views import index, login

urlpatterns = [
    path('home/', index, name='home'),  # root URL will redirect to index
    path('', login, name='login'),
]
