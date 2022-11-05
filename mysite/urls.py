"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from register import views as v
from django.conf import settings
from django.conf.urls.static import static


# This line means that for every URL that starts with admin/, Django will find a corresponding view.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',v.register, name="register"),
    path('', include('blog.urls')),
    path('', include("django.contrib.auth.urls")),
    path('myspace/', include("userprofile.urls")),
    path('learning/', include("quiz.urls")),
    path('activity/', include("activity.urls")),
    path('tinymce/', include('tinymce.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

