from django.urls import path
from . import views

urlpatterns = [
    path('', views.movielist),
    path('bestFive/', views.bestFive),
    path('<int:movie_id>/', views.moviedetail),
    path('<int:movie_id>/reviews/', views.reviews_create),
    path('<int:review_pk>/review_delete/', views.review_delete),
    path('forUserMovieSave/', views.forUserMovieSave),
]
