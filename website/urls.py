from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
	path('',views.res_view,name='res'),
    path('admin/', admin.site.urls),    
]

