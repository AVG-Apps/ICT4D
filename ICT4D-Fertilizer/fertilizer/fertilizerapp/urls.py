from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    path('<int:fertilizer_id>/', views.detail, name='detail'),
    path('<int:fertilizer_id>/results/', views.results, name='results'),
    path('<int:fertilizer_id>/edit/', views.edit, name='edit'),
    path('new_fertilizer', views.add, name='add'),
]