import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_try.settings')
django.setup()

from main_app.models import atlas_data, cell_atlas  # 替换为你的模型

""" # 读取 Excel 文件
df = pd.read_excel('your_excel_file.xlsx')  # 替换为你的文件名

for _, row in df.iterrows():
    atlas_data.objects.create(
        accession=row['accession'],
        species=row['species'],
        classes=row['classes'],
        cells=row['cells'],
        samples=row['samples'],
        platform=row['platform'],
        abstract=row.get('abstract', ''),
        link=row['link']
    )

print("数据导入完成！") """


# 读取 Excel 文件
df = pd.read_excel('UMAP_cluster_DEGs.xlsx')  # 请将文件名替换为你的实际文件名
print(df.columns)
# 遍历每一行并写入数据库
for _, row in df.iterrows():
    cell_atlas.objects.create(
        cell_type=row['cluster'],
        gene=row['gene'],
        avg_log2FC=row['avg_log2FC'],
        pct_1=row['pct.1'],
        pct_2=row['pct.2'],
        p_value=row['p_val'],
        p_val_adj=row['p_val_adj']
    )

print("cell_atlas 数据导入完成！")