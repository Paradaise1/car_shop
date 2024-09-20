from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.IndexListView.as_view(),
         name='index'),
    path('cars/create/', views.CarCreateView.as_view(),
         name='create_car'),
    path('cars/<int:car_id>/', views.CarDetailView.as_view(),
         name='car_detail'),
    path('cars/<int:car_id>/edit/', views.CarUpdateView.as_view(),
         name='edit_car'),
    path('cars/<int:car_id>/delete/', views.CarDeleteView.as_view(),
         name='delete_car'),
    path('cars/<int:car_id>/comment/', views.CommentCreateView.as_view(),
         name='add_comment'),
]
