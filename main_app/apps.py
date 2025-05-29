from django.apps import AppConfig
#这个文件是用来配置应用程序的，主要是定义应用程序的名称和一些其他的配置选项。每个Django应用程序都应该有一个apps.py文件，用于定义应用程序的配置类。

class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
