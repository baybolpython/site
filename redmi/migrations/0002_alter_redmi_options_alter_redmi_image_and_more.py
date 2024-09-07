# Generated by Django 5.1 on 2024-08-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redmi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='redmi',
            options={'verbose_name': 'Redmi', 'verbose_name_plural': 'Редми'},
        ),
        migrations.AlterField(
            model_name='redmi',
            name='image',
            field=models.ImageField(upload_to='redmi_images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='redmi',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='redmi',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='redmi',
            name='specifications',
            field=models.TextField(verbose_name='Характеристека'),
        ),
    ]
