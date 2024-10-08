# Generated by Django 5.1 on 2024-09-07 09:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redmi', '0003_redmi_sim_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xiaomi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='redmi',
            options={'verbose_name': 'Redmi', 'verbose_name_plural': 'редми'},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('redmi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xiaomi_comment', to='redmi.xiaomi')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
        migrations.AddField(
            model_name='redmi',
            name='xiaomi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='redmi.xiaomi'),
        ),
    ]
