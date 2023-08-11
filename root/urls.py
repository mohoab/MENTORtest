from django.urls import path as pt
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='root'


urlpatterns = [
    pt('',views.home , name='home'),
]

