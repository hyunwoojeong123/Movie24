from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_pk>/',views.article_detail_update_delete),
    path('<int:article_pk>/comments/', views.comment_list_create),
    path('<int:comment_pk>/comments_delete/', views.comment_delete),
    path('<int:user_pk>/profile_articles/', views.profile_articles),
    path('<int:user_pk>/profile_comments/', views.profile_comments),
    path('<int:article_pk>/read/', views.read),
]