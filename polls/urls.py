from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detail, name = 'detail'),
    path('<int:pk>/results/', views.results, name = 'results'),
    path('<int:pk>/vote/', views.vote, name = 'vote'),
    #path('specifics/<int:question_id>/', views.detail, name='detail'),
]