from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#URLS DE LA APLICACION
urlpatterns = [
    path('',views.home_view, name="home"),
    path('configuracion/',views.configuracion_view, name="configuracion"),
    path('desarrollo/',views.desarrollo_view, name="desarrollo"),  
    
     #PARA ACCESO DE USUARIO
    path('usuario/nuevo/',views.nuevo_usuario, name="nuevo_usuario"),
    path('ingresar/',views.ingresar, name="ingresar"),
    path('privado/',views.privado, name="privado"),
    #para cerrar la sesion
    path('cerrar/',views.cerrar, name="cerrar"),     
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)