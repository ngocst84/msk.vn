from django.urls import path
from .views import ViewIndex

app_name = 'testapp'

urlpatterns = [
    path('', ViewIndex.as_view()),
]