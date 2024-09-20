from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.urls import reverse, reverse_lazy

from .forms import CarForm, CommentForm
from .mixins import CarDispatchMixin
from .constans import DISPLAYED_CARS
from .models import Car, Comment


User = get_user_model()


def get_query_set(model_objects):
    '''Get basic object's queryset.'''
    return model_objects.select_related('owner').annotate(
        comment_count=Count('comments')
    )


class IndexListView(ListView):
    '''View for main page.'''
    model = Car
    template_name = 'shop/index.html'

    queryset = get_query_set(Car.objects).order_by(
        '-updated_at', '-created_at'
    )

    paginate_by = DISPLAYED_CARS


class CarDetailView(DetailView):
    '''View for detail car's information.'''
    model = Car
    template_name = 'shop/detail.html'

    def get_queryset(self):
        return get_query_set(Car.objects)

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(), pk=self.kwargs.get('car_id')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.select_related('author')
        return context


class CarCreateView(LoginRequiredMixin, CreateView):
    '''View for creating car.'''
    model = Car
    template_name = 'shop/create.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse('shop:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarUpdateView(CarDispatchMixin, UpdateView):
    '''View for modifying car.'''
    model = Car
    template_name = 'shop/create.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse(
            'shop:car_detail', kwargs={'car_id': self.kwargs.get('car_id')}
        )

    def get_object(self):
        return get_object_or_404(
            Car,
            pk=self.kwargs.get('car_id'),
            owner=self.request.user
        )


class CarDeleteView(CarDispatchMixin, DeleteView):
    '''View for deleting car.'''
    model = Car
    template_name = 'shop/create.html'
    queryset = Car.objects.all()
    success_url = reverse_lazy('shop:index')

    def get_object(self):
        return get_object_or_404(
            self.queryset,
            pk=self.kwargs.get('car_id'),
            owner=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object
        context['form'] = CarForm(
            self.request.POST, instance=instance
        )
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    '''View for creating comment.'''
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse(
            'shop:car_detail', kwargs={'car_id': self.kwargs.get('car_id')}
        )

    def get_object(self):
        car = get_object_or_404(
            Car,
            pk=self.kwargs.get('car_id'),
        )
        return car

    def form_valid(self, form):
        form.instance.car = self.get_object()
        form.instance.author = self.request.user
        return super().form_valid(form)
