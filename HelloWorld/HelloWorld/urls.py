"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views,testdb
handler404 = testdb.page_not_found
handler500 = testdb.page_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login1/', views.login),
    path('index/', testdb.index),
    path('login/', testdb.testdb),
    path('sign/',testdb.sign),
    path('rtin/',testdb.rtin),
    path('logout/', testdb.logout),
    path('Rindex/', testdb.Rindex),
    path('upload/', testdb.upload),
    path('serch/', testdb.SerchId),
    path('user/', testdb.SerchIdDetials),
    
    
]
