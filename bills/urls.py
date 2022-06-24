from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api_1/', views.GetOneEndPointView.as_view()),
    path('api_2/', views.GetTwoEndPointView.as_view()),
    path('api_3/', views.GetThreeEndPointView.as_view()),
 ]
