from django.contrib import admin
from django.urls import path,include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.res_view,name='res'),
    path('admin/', admin.site.urls),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)