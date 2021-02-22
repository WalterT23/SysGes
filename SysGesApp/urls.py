from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#URLS DE LA APLICACION
urlpatterns = [
    path('',views.home_view, name="home"),
    path('configuracion/',views.configuracion_view, name="configuracion"),
    path('desarrollo/',views.desarrollo_view, name="desarrollo"),  
    
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)