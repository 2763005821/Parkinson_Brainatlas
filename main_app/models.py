from django.db import models

# Create your models here.
#编写数据库模型类

class cell_atlas(models.Model):
    #定义数据库表的字段
    cell_type = models.CharField(max_length=100)  #细胞类型
    gene = models.CharField(max_length=100)  #基因名称
    avg_log2FC = models.FloatField()  #平均Log2 Fold Change
    pct_1 = models.FloatField()  #百分比1
    pct_2 = models.FloatField()  #百分比2
    p_value = models.FloatField()  #p值
    p_val_adj = models.FloatField()  #调整后的p值

    def __str__(self):
        return self.cell_id
    

class atlas_data(models.Model):
    #定义数据库表的字段
    accession = models.CharField(max_length=100)  #数据集名称
    species = models.CharField(max_length=100)  #物种
    classes = models.CharField(max_length=100)  #分类
    cells = models.IntegerField()  #细胞数
    samples = models.IntegerField()  #样本数
    platform = models.CharField(max_length=100)  #平台
    abstract = models.TextField(default='')  #摘要
    link = models.URLField()  #链接
    
    def __str__(self):
        return self.ID
    
class user(models.Model):
    #定义数据库表的字段
    user_name = models.CharField(max_length=100)  #用户名
    password = models.CharField(max_length=100)  #密码
    email = models.EmailField()  #邮箱

    def __str__(self):
        return self.user_name
