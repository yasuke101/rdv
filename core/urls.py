from django.urls import path
from . import views

urlpatterns = [
    path('RDV/',views.res_view,name='res'),
   

]