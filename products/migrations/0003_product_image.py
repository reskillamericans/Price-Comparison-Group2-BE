# Generated by Django 3.2.4 on 2021-07-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210731_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='DEFAULT VALUE', max_length=300),
        ),
    ]