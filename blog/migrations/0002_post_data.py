# Generated by Django 3.1.4 on 2021-04-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]