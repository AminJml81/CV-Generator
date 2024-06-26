from cv import views
from django.urls import path


urlpatterns = [
    path('', views.cv_view, name='index')
]
