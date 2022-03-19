from django.urls import path

from .views import MovieViewSet


urlpatterns = [
    path("api/movies/", MovieViewSet.as_view({'get': 'list'})),
    path("api/movies/<int:pk>/", MovieViewSet.as_view({'get': 'get'})),
    ]
