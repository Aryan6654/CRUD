# Generated by Django 3.1.4 on 2021-07-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adduser',
            name='name',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
        migrations.AddField(
            model_name='adduser',
            name='password',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]