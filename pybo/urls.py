from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/edit/<int:question_id>/', views.question_edit, name='question_edit'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
]