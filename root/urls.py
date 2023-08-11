from django.urls import path as pt
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='root'


urlpatterns = [
    pt('',views.home , name='home')
]

urlpatterns += static(settings.MEDIA_URL , DUCUMENT_ROOT=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL , DUCUMENT_ROOT=settings.STATIC_ROOT)