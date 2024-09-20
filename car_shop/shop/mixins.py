from django.http import Http404
from django.shortcuts import redirect

from .models import Car


class CarDispatchMixin:
    '''Mixin for overriding the default dispatch method
    to include custom logic for car's generic views.'''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('shop:car_detail', **kwargs)
        try:
            Car.objects.get(pk=self.kwargs.get('car_id'))
        except Car.DoesNotExist:
            raise Http404
        try:
            Car.objects.get(
                pk=self.kwargs.get('car_id'), owner=self.request.user
            )
            return super().dispatch(request, *args, **kwargs)
        except Car.DoesNotExist:
            return redirect('shop:car_detail', **kwargs)
