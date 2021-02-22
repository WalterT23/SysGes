from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

#URLS DE LA APLICACION
urlpatterns = [
    path('',views.administracion_view, name="administracion"),
]