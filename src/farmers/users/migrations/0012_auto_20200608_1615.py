# Generated by Django 3.0.6 on 2020-06-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200608_0022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.AlterField(
            model_name='user',
            name='surname',
            field=models.CharField(max_length=150, verbose_name='surname'),
        ),
    ]
