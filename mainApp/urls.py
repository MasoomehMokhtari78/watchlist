from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addnew', views.addNew),
    path('update/<int:pk>', views.updateMovie, name='update_movie'),
    path('delete/<int:pk>', views.deleteMovie, name='delete_movie'),
]

