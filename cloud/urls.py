"""cloud URL Configuration

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
from django.urls import path,include
from cloud.core import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.Home.as_view(), name='home'),
 path('books/', views.upload_book, name='upload_book'),
      path('book_list/', views.book_list, name='book_list'),
 path('book_list/<int:pk>/', views.delete_book, name='delete_book'),

    path('admin/', admin.site.urls),
     path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
   	

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

