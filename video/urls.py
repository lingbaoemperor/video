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
from django.urls import path
from show_video import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.init),
    path('list/', views.list_page),
    path('list/switch_to_upload/', views.switch_to_upload),
    path('upload/', views.upload),
    path('list/play/', views.play),
#	url(r'^login/$',views.init),
#	url(r'^check/$',views.check),
#	url(r'^list_page/$',views.list_page),
]
#链接访问图片
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
