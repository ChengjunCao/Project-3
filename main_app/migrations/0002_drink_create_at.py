# Generated by Django 3.1.5 on 2021-02-01 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-02-01'),
            preserve_default=False,
        ),
    ]
