# Generated by Django 4.2.4 on 2023-08-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='teacher',
            field=models.CharField(max_length=100),
        ),
    ]
