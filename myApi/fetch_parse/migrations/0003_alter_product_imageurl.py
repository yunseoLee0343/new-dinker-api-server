# Generated by Django 5.0.4 on 2024-04-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_parse', '0002_product_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageUrl',
            field=models.URLField(default='https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000002487]_20210426091745609.jpg', max_length=100),
        ),
    ]
