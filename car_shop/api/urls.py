from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CarViewSet, CommentViewSet

app_name = 'api'

cars_router = DefaultRouter()
cars_router.register('cars', CarViewSet, basename='cars')

comment_router = DefaultRouter()
comment_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(cars_router.urls)),
    path('cars/<int:car_id>/', include(comment_router.urls)),
]
