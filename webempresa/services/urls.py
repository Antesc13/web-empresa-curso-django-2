from django.urls import path
from . import views
urlpatterns = [
    #paths del services
   
    path('services/', views.services, name="services"),
  

]
