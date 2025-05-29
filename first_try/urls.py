"""
URL configuration for first_try project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

#需要从创建的app文件夹中导入views.py文件中的视图函数
from main_app import views
from django.urls import path,include
from main_app.views import CellAtlasListView
urlpatterns = [
    path('admin/', admin.site.urls),
    #（2）配置网站与页面的映射关系
    path('index/', views.index),  #访问网站的index页面，映射到main_app/views.py中的index函数执行并返回index.html页面
    path('user/', views.user_view),  #访问网站的user页面，映射到main_app/views.py中的user函数执行并返回user.html页面
    #案例：用户信息管理系统
    path('info/add/', views.info_add, name='info_add'),
    path('cellatlas/', CellAtlasListView.as_view(), name='cellatlas-list'),
    path('api/', include('main_app.urls')),  # ← 加这一行
]
