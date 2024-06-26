# Generated by Django 5.0.4 on 2024-05-27 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('NEWS', 'Новость'), ('ARTICLE', 'Статья')], default='NEWS', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_type', to='djangoproject.category'),
        ),
    ]
