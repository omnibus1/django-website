
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns=[
    
    path("",views.home,name="home"),
    # path("outlet/",views.outlet,name="outlet"),
    path("Socket/",views.socket,name="socket"),
    # path("random/",views.random,name="random"),
    path("Socket_1/on",views.on,name="on"),
    path("Socket_1/off",views.off,name="off"),
    path("zdjecia/",views.zdjecia,name="zdjecia")

]
urlpatterns += staticfiles_urlpatterns()