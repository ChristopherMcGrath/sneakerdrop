# Generated by Django 3.1.2 on 2020-11-15 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_auto_20201115_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='image',
            field=models.ImageField(upload_to='assets/images'),
        ),
    ]