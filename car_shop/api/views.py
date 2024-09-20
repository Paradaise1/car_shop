from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from api.serializers import (
    CarSerializer,
    CommentSerializer,
)
from api.permissions import IsOwnerOrReadOnly
from shop.models import Car


def get_car(obj):
    '''Get a car object'''
    return get_object_or_404(Car, id=obj.kwargs.get('car_id'))


class CarViewSet(viewsets.ModelViewSet):
    '''ViewSet for cars.'''
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    http_method_names = ['get', 'post', 'put', 'delete']
    lookup_url_kwarg = 'car_id'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, updated_at=None)


class CommentViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    '''ViewSet for comments.'''
    serializer_class = CommentSerializer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return get_car(self).comments.all()

    def perform_create(self, serializer):
        car = get_car(self)
        serializer.save(author=self.request.user, car=car)
