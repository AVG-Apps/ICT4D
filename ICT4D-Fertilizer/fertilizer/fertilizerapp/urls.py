from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('results', views.results, name='results'),
    path('add', views.add, name='add'),

    # path('<int:fertilizer_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:fertilizer_id>/results/', views.results, name='results'),
]