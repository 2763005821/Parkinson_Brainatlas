# main_app/views.py
#redirect包负责重定向到其他页面
from django.shortcuts import render, HttpResponse, redirect

#编写views.py文件，定义视图函数
def index(request):
    #（1）定义视图函数，返回index.html页面
    #return render(request, 'index.html')
    return HttpResponse("Hello, world!")

def user(request):
    #（2）定义视图函数，返回user.html页面
    #默认情况下，Django会在每个app的templates目录中查找模板文件，因此我们需要在main_app目录下创建一个templates目录，并在其中创建index.html和user.html文件。

    return HttpResponse("登陆成功")

from main_app.models import cell_atlas, atlas_data, user
#（3）导入模型类cell_atlas、atlas_data和user
def cell_atlas_view(request):
    #（3）定义视图函数，返回cell_atlas.html页面
    cell_atlas_list = cell_atlas.objects.all()
    return render(request, 'cell_atlas.html', {'cell_atlas_list': cell_atlas_list})

def user_view(request):       
    user.objects.create(user_name='fyc', password='2314499817', email='2763005821@qq.com')
    #（4）定义视图函数，返回数据
    user_list = user.objects.all()
    user.objects.filter(id__gt=1).delete()  # 删除id大于1的用户
    return HttpResponse(user_list,user.objects.all())

def info_list(request):
    # 1.获取数据库中的所有数据
    data_list = user.objects.all()
    print(data_list)

def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        user.objects.create(user_name=name, password=pwd, email=email)
        return HttpResponse("信息添加成功")
    return render(request, 'info_add.html')

##########################################################
from rest_framework import generics
from .models import cell_atlas
from .serializers import CellAtlasSerializer

class CellAtlasListView(generics.ListAPIView):
    queryset = cell_atlas.objects.all()
    serializer_class = CellAtlasSerializer

    def get_queryset(self):
        queryset = cell_atlas.objects.all()
        gene = self.request.query_params.get('gene')
        if gene:
            queryset = queryset.filter(gene__icontains=gene)  # 关键字模糊匹配
        return queryset
