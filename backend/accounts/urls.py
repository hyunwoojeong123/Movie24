from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('<int:user_pk>/', views.takename),
    path('signup/',views.signup),
    path('<int:user_pk>/recommend/', views.recommend),
    path('<int:user_pk>/points/', views.points),
    # jwt가 대신 login해줌...
    path('api-token-auth/',obtain_jwt_token),
]