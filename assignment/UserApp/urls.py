from django.urls import path,include
from . import views

app_name = 'UserApp'

urlpatterns = [
path('', views.homeView, name='homeUrl'),
path('post-submit', views.postSubmitView, name='postSubmitUrl'),
]