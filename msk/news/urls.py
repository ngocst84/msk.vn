from django.urls import path
from .views import ViewIndex

app_name = 'news'

urlpatterns = [
    path('', ViewIndex.as_view()),
]