"""video URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from show_video import views as video_views
from user import views as user_views
from django.views.static import serve
from video.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.init),
    path('list/',  user_views.list_page),
    path('register/', user_views.register),
   
    path('video/', user_views.video),
    path('novel/',user_views.novel),

    path('upload/', video_views.upload),
    path('video/play/<int:video>/',video_views.play),
   #？字符串传参，视图函数用get获取
   # re_path(r'^play/(?P<video>[\w]+)/$',video_views.play),

    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
]
#链接访问图片
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
