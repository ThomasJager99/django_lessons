from django.urls import path
from haru.views import sumimasen_desuka

urlpatterns = [
    path('', sumimasen_desuka, name='hallo')
]