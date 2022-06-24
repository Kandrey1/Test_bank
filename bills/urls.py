from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api_load_client/', views.LoadClientView.as_view()),
    path('api_load_organization/', views.LoadOrganizationView.as_view()),
    path('api_load_bills/', views.LoadBillsView.as_view()),
    path('api_2/', views.GetTwoEndPointView.as_view()),
    path('api_3/', views.GetThreeEndPointView.as_view()),
 ]
